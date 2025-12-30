from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpFormRequestGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        use_cases = contract.get("use_cases", {})
        if not use_cases:
            return []

        entities = contract.get("entities", {})
        db_config = contract.get("database", {})
        
        generated_files = []
        for uc_name, uc_def in use_cases.items():
            inputs = uc_def.get("input", {})
            if inputs:
                generated_files.append(self._generate_form_request(uc_name, uc_def, entities, db_config, output_dir))
            
        return generated_files

    def _generate_form_request(self, uc_name: str, uc_def: dict, entities: dict, db_config: dict, output_dir: Path):
        base_ns = self.config.project_namespace
        
        # We'll put requests in Infrastructure/Http/Requests
        req_suffix = "Infrastructure/Http/Requests"
        target_ns = f"{base_ns}\\{req_suffix.replace('/', '\\')}"
        target_dir = output_dir / req_suffix
        target_dir.mkdir(parents=True, exist_ok=True)

        class_name = f"{uc_name}Request"
        inputs = uc_def.get("input", {})
        rules = uc_def.get("rules", [])
        
        entity_name = uc_def.get("entity")
        if not entity_name and entities:
            entity_name = list(entities.keys())[0]
            
        table_name = "TODO_TABLE"
        if entity_name and entity_name in entities:
             # This is a bit simplified, ideally we have a way to get table name for any entity
             table_name = db_config.get("table", entity_name.lower() + "s")

        validation_rules = {}
        for field_name, field_type in inputs.items():
            is_nullable = field_name.endswith("?")
            clean_field_name = field_name.replace("?", "")
            
            field_rules = []
            if is_nullable:
                field_rules.append("nullable")
            else:
                field_rules.append("required")
                
            # Type mapping
            clean_type = field_type.replace("?", "") if isinstance(field_type, str) else field_type.get("type", "string").replace("?", "")
            
            type_map = {
                "string": "string",
                "int": "integer",
                "integer": "integer",
                "float": "numeric",
                "number": "numeric",
                "bool": "boolean",
                "boolean": "boolean",
                "datetime": "date",
                "date": "date",
                "array": "array"
            }
            
            if clean_type in type_map:
                field_rules.append(type_map[clean_type])
            
            # Extract rules from use case rules section
            for rule_def in rules:
                if "ensure" in rule_def:
                    ensure_rule = rule_def["ensure"]
                    if f"{clean_field_name} matches" in ensure_rule:
                        regex = ensure_rule.split("matches")[-1].strip()
                        field_rules.append(f"regex:{regex}")
                    if f"{clean_field_name} is_unique" in ensure_rule:
                        field_rules.append(f"unique:{table_name},{clean_field_name}")
            
            validation_rules[clean_field_name] = field_rules

        template = self.load_template("form_request.php.tpl")
        context = {
            "namespace": target_ns,
            "class_name": class_name,
            "validation_rules": validation_rules
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{class_name}.php"
        file_path.write_text(content)
        return file_path
