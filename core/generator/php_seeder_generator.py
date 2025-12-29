from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpSeederGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entities = contract.get("entities", {})
        generated_files = []
        
        base_ns = self.config.project_namespace
        model_ns = f"{base_ns}\\Infrastructure\\Persistence\\Eloquent"
        
        for entity_name in entities:
            context = {
                "class_name": entity_name,
                "model_import": f"{model_ns}\\{entity_name}"
            }
            
            template = self.load_template("seeder.php.tpl")
            content = self.render(template, context)
            
            seeder_dir = output_dir.parent / "database" / "seeders"
            seeder_dir.mkdir(parents=True, exist_ok=True)
            
            file_path = seeder_dir / f"{entity_name}Seeder.php"
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files
