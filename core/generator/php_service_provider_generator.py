from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpServiceProviderGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entities = contract.get("entities", {})
        if not entities:
            return []
            
        base_ns = self.config.project_namespace
        provider_suffix = "Infrastructure/Laravel"
        namespace = f"{base_ns}\\{provider_suffix.replace('/', '\\')}"
        
        repo_impl_ns = f"{base_ns}\\Infrastructure\\Persistence\\Eloquent"
        interface_ns_suffix = self.config.get_generator_config("repository").get("interface_namespace_suffix", "Domain/Repository")
        repo_interface_ns = f"{base_ns}\\{interface_ns_suffix.replace('/', '\\')}"
        
        bindings = []
        for entity_name in entities:
            interface_name = f"{entity_name}Repository"
            impl_name = f"Eloquent{entity_name}Repository"
            
            bindings.append({
                "interface": f"{repo_interface_ns}\\{interface_name}",
                "interface_name": interface_name,
                "implementation": f"{repo_impl_ns}\\{impl_name}",
                "implementation_name": impl_name
            })
            
        context = {
            "namespace": namespace,
            "class_name": f"{contract['module']['name']}ServiceProvider",
            "bindings": bindings
        }
        
        template = self.load_template("service_provider.php.tpl")
        content = self.render(template, context)
        
        target_dir = output_dir / provider_suffix
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_name = f"{contract['module']['name']}ServiceProvider.php"
        file_path = target_dir / file_name
        file_path.write_text(content)
        
        return [file_path]
