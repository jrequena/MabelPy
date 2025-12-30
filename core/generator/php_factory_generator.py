from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpFactoryGenerator(BaseGenerator):
    FAKER_MAP = {
        "int": "fake()->randomNumber()",
        "string": "fake()->word()",
        "email": "fake()->safeEmail()",
        "datetime": "fake()->dateTime()",
        "bool": "fake()->boolean()",
        "Uuid": "fake()->uuid()",
    }

    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entities = contract.get("entities", {})
        generated_files = []
        
        base_ns = self.config.project_namespace
        model_ns = f"{base_ns}\\Infrastructure\\Persistence\\Eloquent"
        
        for entity_name, fields in entities.items():
            factory_fields = self._prepare_factory_fields(fields)
            
            context = {
                "class_name": entity_name,
                "model_import": f"{model_ns}\\{entity_name}",
                "fields": factory_fields
            }
            
            template = self.load_template("factory.php.tpl")
            content = self.render(template, context)
            
            # Factories go to database/factories outside src
            factory_dir = output_dir.parent / "database" / "factories"
            factory_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = factory_dir / f"{entity_name}Factory.php"
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files

    def _prepare_factory_fields(self, fields: dict) -> list:
        lines = []
        for name, f_def in fields.items():
            if name == "id":
                continue
            
            f_type = "string"
            if isinstance(f_def, dict):
                if "belongs_to" in f_def:
                    target = f_def["belongs_to"]
                    lines.append({
                        "name": f"{target.lower()}_id",
                        "faker_line": f"\\Infrastructure\\Persistence\\Eloquent\\{target}::factory()"
                    })
                    continue
                if "has_many" in f_def or "has_one" in f_def:
                    continue
                f_type = f_def.get("type", "string")
                if name == "email":
                    f_type = "email"
            else:
                f_type = f_def
                if name == "email":
                    f_type = "email"
                
            faker = self.FAKER_MAP.get(f_type, "fake()->word()")
            lines.append({"name": name, "faker_line": faker})
            
        return lines

