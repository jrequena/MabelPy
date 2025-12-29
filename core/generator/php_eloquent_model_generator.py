from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpEloquentModelGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entities = contract.get("entities", {})
        generated_files = []
        
        base_ns = self.config.project_namespace
        model_suffix = "Infrastructure/Persistence/Eloquent"
        namespace = f"{base_ns}\\{model_suffix.replace('/', '\\')}"
        
        for entity_name, fields in entities.items():
            table_name = entity_name.lower() + "s"
            if entity_name == "User": table_name = "users"
            
            fillable = []
            relationships = []
            imports = set()
            
            for name, f_def in fields.items():
                if name == "id": continue
                
                if isinstance(f_def, dict):
                    if "belongs_to" in f_def:
                        target = f_def["belongs_to"]
                        relationships.append({
                            "name": target.lower(),
                            "method": "belongsTo",
                            "return_type": "\\Illuminate\\Database\\Eloquent\\Relations\\BelongsTo",
                            "target_class": target
                        })
                        fillable.append(f"{target.lower()}_id")
                        continue
                    if "has_many" in f_def:
                        target = f_def["has_many"]
                        relationships.append({
                            "name": name,
                            "method": "hasMany",
                            "return_type": "\\Illuminate\\Database\\Eloquent\\Relations\\HasMany",
                            "target_class": target
                        })
                        continue
                    if "has_one" in f_def:
                        target = f_def["has_one"]
                        relationships.append({
                            "name": name,
                            "method": "hasOne",
                            "return_type": "\\Illuminate\\Database\\Eloquent\\Relations\\HasOne",
                            "target_class": target
                        })
                        continue
                
                fillable.append(name)
            
            context = {
                "namespace": namespace,
                "class_name": entity_name,
                "table_name": table_name,
                "fillable": fillable,
                "relationships": relationships,
                "imports": sorted(list(imports))
            }
            
            template = self.load_template("eloquent_model.php.tpl")
            content = self.render(template, context)
            
            target_dir = output_dir / model_suffix
            target_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = target_dir / f"{entity_name}.php"
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files
