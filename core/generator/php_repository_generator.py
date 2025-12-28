from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpRepositoryGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        template = self.load_template("repository_interface.php.tpl")
        
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        
        # Domain Interface
        repo_config = self.config.get_generator_config("repository")
        interface_suffix = repo_config.get("interface_namespace_suffix", "Domain/Repository")
        namespace = f"{base_ns}\\{interface_suffix.replace('/', '\\')}"
        
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        entity_import = f"{base_ns}\\{domain_suffix.replace('/', '\\')}\\{entity_name}"
        
        context = {
            "namespace": namespace,
            "class_name": f"{entity_name}Repository",
            "entity_name": entity_name,
            "entity_import": entity_import
        }
        
        content = self.render(template, context)
        
        target_dir = output_dir / interface_suffix
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / f"{entity_name}Repository.php"
        file_path.write_text(content)
        return file_path
