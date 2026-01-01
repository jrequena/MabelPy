from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class OpenApiGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/docs")
        self.config = config
        self.add_filter("to_openapi_type", self.to_openapi_type)

    def generate(self, contract: dict, output_dir: Path):
        use_cases = contract.get("use_cases", {})
        entities = contract.get("entities", {})
        self.contract = contract # Store for filter
        
        # Prepare context
        prepared_use_cases = {}
        for name, uc in use_cases.items():
            entity_name = uc.get("entity", list(entities.keys())[0] if entities else "Default")
            is_list = name.startswith(("List", "GetAll", "Search"))
            prepared_use_cases[name] = {
                **uc,
                "is_list": is_list,
                "entity": entity_name,
                "entity_path": entity_name.lower().replace("_", "-"),
                "name_path": name.lower().replace("_", "-")
            }

        template = self.load_template("openapi.yaml.tpl")
        context = {
            "project_name": self.config.project_name,
            "version": contract.get("metadata", {}).get("version", "1.0.0"),
            "use_cases": prepared_use_cases,
            "entities": entities
        }
        
        content = self.render(template, context)
        target_dir = output_dir / "docs"
        target_dir.mkdir(parents=True, exist_ok=True)
        file_path = target_dir / "openapi.yaml"
        file_path.write_text(content)
        return [file_path]

    def to_openapi_type(self, type_str):
        if not isinstance(type_str, str):
            type_str = type_str.get("type", "string")
            
        is_nullable = "?" in type_str
        type_str = type_str.replace("?", "")
        
        # Check if it's an entity or enum
        if type_str in self.contract.get("entities", {}) or type_str in self.contract.get("enums", {}):
            return f"$ref: '#/components/schemas/{type_str}'"
        
        mapping = {
            "string": "type: string",
            "int": "type: integer",
            "integer": "type: integer",
            "float": "type: number\n          format: float",
            "number": "type: number",
            "bool": "type: boolean",
            "boolean": "type: boolean",
            "datetime": "type: string\n          format: date-time",
            "date": "type: string\n          format: date"
        }
        
        res = mapping.get(type_str, "type: string")
        if is_nullable:
            res += "\n          nullable: true"
        return res
