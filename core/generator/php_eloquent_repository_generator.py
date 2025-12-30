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
        
        for entity_name in entities:
            interface_name = f"{entity_name}Repository"
            model_name = entity_name
            class_name = f"Eloquent{entity_name}Repository"
            
            interface_import = f"{base_ns}\\{interface_ns_suffix.replace('/', '\\')}\\{interface_name}"
            model_import = f"{namespace}\\{model_name}"
            
            context = {
                "namespace": namespace,
                "class_name": class_name,
                "interface_name": interface_name,
                "interface_import": interface_import,
                "model_name": model_name,
                "model_import": model_import,
                "imports": []
            }
            
            template = self.load_template("eloquent_repository.php.tpl")
            content = self.render(template, context)
            
            target_dir = output_dir / repo_impl_suffix
            target_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = target_dir / f"{class_name}.php"
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files
