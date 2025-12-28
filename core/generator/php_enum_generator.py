from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpEnumGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, name: str, enum_def: dict, output_dir: Path):
        template = self.load_template("enum.php.tpl")
        
        base_ns = self.config.project_namespace
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        namespace = f"{base_ns}\\{domain_suffix.replace('/', '\\')}\\Enum"
        
        values = []
        for val in enum_def["values"]:
            values.append({
                "case": val.upper().replace('-', '_').replace(' ', '_'),
                "value": val
            })
            
        context = {
            "namespace": namespace,
            "class_name": name,
            "values": values
        }
        
        content = self.render(template, context)
        
        target_dir = output_dir / domain_suffix / "Enum"
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / f"{name}.php"
        file_path.write_text(content)
        return file_path
