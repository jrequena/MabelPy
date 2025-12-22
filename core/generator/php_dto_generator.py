from pathlib import Path
from core.generator.base_generator import BaseGenerator

class PhpDtoGenerator(BaseGenerator):
    def __init__(self):
        super().__init__("core/templates/php")

    def generate(self, contract: dict, output_dir: str):
        template = self.load_template("dto.php.tpl")

        context = {
            "namespace": "App",
            "class_name": contract["entity"]["name"] + "Dto",
            "fields": contract["fields"],
        }

        content = self.render(template, context)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / f"{context['class_name']}.php"
        file_path.write_text(content)

        return file_path
