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

        # 1. Entity Documentation
        self._generate_entity_doc(contract, entity_doc_dir)

        # 2. Use Case Documentation
        self._generate_use_case_docs(contract, entity_doc_dir)

    def _generate_entity_doc(self, contract: dict, target_dir: Path):
        template = self.load_template("entity_doc.md.tpl")
        
        fields_data = []
        for f in contract.get("fields", []):
            fields_data.append({
                "name": f["name"],
                "type": f["type"],
                "nullable": "Yes" if f.get("nullable") else "No",
                "validation": f.get("validation", "None"),
                "description": f.get("description", "No description provided.")
            })

        context = {
            "entity_name": contract["entity"]["name"],
            "description": contract["entity"].get("description", "Core domain entity."),
            "fields": fields_data
        }

        # We need to use 'field' loop name for BaseGenerator to recognize it
        # Actually BaseGenerator expects 'fields' in context and 'field' in template
        context["fields"] = fields_data
        
        # Override render to handle field specifically if needed, 
        # but BaseGenerator already does it.
        # However, BaseGenerator only replaces specific keys in 'field'
        
        content = self._custom_render(template, context)
        (target_dir / "Entity.md").write_text(content)

    def _generate_use_case_docs(self, contract: dict, target_dir: Path):
        template = self.load_template("use_case_doc.md.tpl")
        entity_name = contract["entity"]["name"]
        
        use_cases = ["Create", "Update", "Get", "Delete", "List"]
        for uc in use_cases:
            class_name = f"{uc}{entity_name}"
            
            # Simple simulation of request/response fields
            request_fields = []
            if uc in ["Create", "Update"]:
                for f in contract.get("fields", []):
                    if f["name"] != "id":
                        request_fields.append({
                            "name": f["name"],
                            "type": f["type"],
                            "required": "Yes" if not f.get("nullable") else "No"
                        })
            
            response_fields = []
            if uc in ["Get", "Create", "Update"]:
                 for f in contract.get("fields", []):
                    response_fields.append({
                        "name": f["name"],
                        "type": f["type"]
                    })
            elif uc == "List":
                response_fields.append({"name": "items", "type": f"List<{entity_name}>"})
            
            context = {
                "class_name": class_name,
                "description": f"Use case to {uc.lower()} a {entity_name}.",
                "repository_name": f"{entity_name}Repository",
                "request_fields": request_fields,
                "response_fields": response_fields
            }
            
            # Custom render because use_case_doc uses request_fields and response_fields
            content = self._render_use_case(template, context)
            (target_dir / f"{class_name}.md").write_text(content)

    def _custom_render(self, template: str, context: dict) -> str:
        # BaseGenerator's field loop is too specific for PHP. 
        # I'll implement a generic loop here or update BaseGenerator.
        # For now, let's do a simple replacement for MD.
        output = template
        output = output.replace("{{ entity_name }}", context["entity_name"])
        output = output.replace("{{ description }}", context["description"])
        
        if "{% for field in fields %}" in output:
            parts = output.split("{% for field in fields %}", 1)
            rest = parts[1].split("{% endfor %}", 1)
            loop_block = rest[0]
            
            rendered_fields = ""
            for f in context["fields"]:
                item_block = loop_block
                item_block = item_block.replace("{{ field.name }}", f["name"])
                item_block = item_block.replace("{{ field.type }}", f["type"])
                item_block = item_block.replace("{{ field.nullable }}", f["nullable"])
                item_block = item_block.replace("{{ field.validation }}", f["validation"])
                item_block = item_block.replace("{{ field.description }}", f["description"])
                rendered_fields += item_block
            
            output = parts[0] + rendered_fields + rest[1]
            
        return output

    def _render_use_case(self, template: str, context: dict) -> str:
        output = template
        output = output.replace("{{ class_name }}", context["class_name"])
        output = output.replace("{{ description }}", context["description"])
        output = output.replace("{{ repository_name }}", context["repository_name"])
        
        # Handle request_fields
        if "{% for field in request_fields %}" in output:
            parts = output.split("{% for field in request_fields %}", 1)
            rest = parts[1].split("{% endfor %}", 1)
            loop_block = rest[0]
            rendered = ""
            for f in context["request_fields"]:
                rendered += loop_block.replace("{{ field.name }}", f["name"])\
                                      .replace("{{ field.type }}", f["type"])\
                                      .replace("{{ field.required }}", f["required"])
            output = parts[0] + rendered + rest[1]

        # Handle response_fields
        if "{% for field in response_fields %}" in output:
            parts = output.split("{% for field in response_fields %}", 1)
            rest = parts[1].split("{% endfor %}", 1)
            loop_block = rest[0]
            rendered = ""
            for f in context["response_fields"]:
                rendered += loop_block.replace("{{ field.name }}", f["name"])\
                                      .replace("{{ field.type }}", f["type"])
            output = parts[0] + rendered + rest[1]
            
        return output
