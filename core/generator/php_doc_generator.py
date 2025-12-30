from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpDocGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/docs")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        if not self.config.get("generators.documentation.enabled", True):
            return

        doc_root = Path(self.config.get("paths.docs", "docs")).absolute()
        entity_name = contract["entity"]["name"]
        entity_doc_dir = doc_root / entity_name
        entity_doc_dir.mkdir(parents=True, exist_ok=True)

        self._generate_entity_doc(contract, entity_doc_dir)
        self._generate_use_case_docs(contract, entity_doc_dir)

    def _generate_entity_doc(self, contract: dict, target_dir: Path):
        template = self.load_template("entity_doc.md.tpl")
        
        fields_data = []
        for f in contract.get("fields", []):
            f_type = f.get("type", "")
            if "has_many" in f:
                f_type = f"Collection<{f['has_many']}>"
            elif "belongs_to" in f:
                f_type = f"Relationship(BelongsTo {f['belongs_to']})"
            elif "has_one" in f:
                f_type = f"Relationship(HasOne {f['has_one']})"

            fields_data.append({
                "name": f["name"],
                "type": f_type,
                "nullable": "Yes" if f.get("nullable") or "belongs_to" in f or "has_one" in f else "No",
                "validation": ", ".join(f.get("validations", [])) if f.get("validations") else "None",
                "description": f.get("description", "No description provided.")
            })

        context = {
            "entity_name": contract["entity"]["name"],
            "description": contract["entity"].get("description", f"Core domain entity for {contract['entity']['name']}."),
            "fields": fields_data
        }

        content = self.render(template, context)
        (target_dir / "Entity.md").write_text(content)

    def _generate_use_case_docs(self, contract: dict, target_dir: Path):
        template = self.load_template("use_case_doc.md.tpl")
        entity_name = contract["entity"]["name"]
        
        use_cases = contract.get("use_cases", {})
        for uc_name, uc_def in use_cases.items():
            if uc_def.get("entity", entity_name) != entity_name:
                continue
                
            req_fields = []
            for name, f_type in uc_def.get("input", {}).items():
                req_fields.append({
                    "name": name.replace("?", ""),
                    "type": f_type.replace("?", ""),
                    "required": "No" if "?" in name or "?" in f_type else "Yes"
                })
            
            res_fields = []
            output = uc_def.get("output", "void")
            if isinstance(output, dict):
                for name, f_type in output.items():
                    res_fields.append({"name": name, "type": f_type})
            elif isinstance(output, str) and output != "void":
                res_fields.append({"name": "data", "type": output})
            
            context = {
                "class_name": uc_name,
                "description": uc_def.get("description", f"Use case for {uc_name}."),
                "repository_name": f"{entity_name}Repository",
                "request_fields": req_fields,
                "response_fields": res_fields
            }
            
            content = self.render(template, context)
            (target_dir / f"{uc_name}.md").write_text(content)
