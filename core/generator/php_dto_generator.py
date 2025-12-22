from pathlib import Path
from core.generator.base_generator import BaseGenerator

class PhpDtoGenerator(BaseGenerator):

    TYPE_MAP = {
        "int": "int",
        "string": "string",
        "bool": "bool",
        "float": "float",
        "datetime": "\\DateTimeImmutable",
    }

    def __init__(self):
        super().__init__("core/templates/php")

    def normalize_fields(self, fields: list) -> list:
        normalized = []

        for field in fields:
            raw_type = field["type"]

            if raw_type not in self.TYPE_MAP:
                raise ValueError(f"Unsupported PHP type: {raw_type}")

            normalized.append({
                "name": field["name"],
                "type": self.TYPE_MAP[raw_type],
            })

        return normalized

    def generate(self, contract: dict, output_dir: str):
        template = self.load_template("dto.php.tpl")

        fields = self.normalize_fields(contract["fields"])

        context = {
            "namespace": "App",
            "class_name": contract["entity"]["name"] + "Dto",
            "fields": fields,
        }

        content = self.render(template, context)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / f"{context['class_name']}.php"
        file_path.write_text(content)

        return file_path
