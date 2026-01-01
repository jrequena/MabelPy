from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpEloquentRepositoryGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entities = contract.get("entities", {})
        generated_files = []
        
        base_ns = self.config.project_namespace
        repo_impl_suffix = "Infrastructure/Persistence/Eloquent"
        namespace = f"{base_ns}\\{repo_impl_suffix.replace('/', '\\')}"
        
        interface_ns_suffix = self.config.get_generator_config("repository").get("interface_namespace_suffix", "Domain/Repository")
        
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        mapper_suffix = self.config.get_generator_config("mapper").get("namespace_suffix", "Infrastructure/Mapper")
        
        for entity_name in entities:
            fields = entities[entity_name]
            
            # Identify relationships for complex save logic
            relationships = []
            for field_name, field_def in fields.items():
                if isinstance(field_def, dict):
                    if "belongs_to" in field_def:
                        relationships.append({
                            "name": field_name,
                            "type": "belongs_to",
                            "target": field_def["belongs_to"]
                        })
                    elif "has_many" in field_def:
                        relationships.append({
                            "name": field_name,
                            "type": "has_many",
                            "target": field_def["has_many"]
                        })
                    elif "has_one" in field_def:
                        relationships.append({
                            "name": field_name,
                            "type": "has_one",
                            "target": field_def["has_one"]
                        })

            interface_name = f"{entity_name}Repository"
            model_name = entity_name
            class_name = f"Eloquent{entity_name}Repository"
            mapper_name = f"{entity_name}Mapper"
            
            interface_import = f"{base_ns}\\{interface_ns_suffix.replace('/', '\\')}\\{interface_name}"
            model_import = f"{namespace}\\{model_name}"
            entity_import = f"{base_ns}\\{domain_suffix.replace('/', '\\')}\\{entity_name}"
            mapper_import = f"{base_ns}\\{mapper_suffix.replace('/', '\\')}\\{mapper_name}"
            
            context = {
                "namespace": namespace,
                "class_name": class_name,
                "interface_name": interface_name,
                "interface_import": interface_import,
                "entity_name": entity_name,
                "entity_import": entity_import,
                "mapper_name": mapper_name,
                "mapper_import": mapper_import,
                "model_name": model_name,
                "model_import": model_import,
                "relationships": relationships,
                "imports": ["Illuminate\\Support\\Facades\\DB"]
            }
            
            template = self.load_template("eloquent_repository.php.tpl")
            content = self.render(template, context)
            
            target_dir = output_dir / repo_impl_suffix
            target_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = target_dir / f"{class_name}.php"
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files
