from pathlib import Path
from core.generator.base_generator import BaseGenerator

class PhpDtoGenerator(BaseGenerator):

    READONLY = True  # ⬅️ activar / desactivar aquí

    TYPE_MAP = {
        "int": {
            "type": "int",
            "import": None,
        },
        "string": {
            "type": "string",
            "import": None,
        },
        "bool": {
            "type": "bool",
            "import": None,
        },
        "float": {
            "type": "float",
            "import": None,
        },
        "datetime": {
            "type": "DateTimeImmutable",
            "import": "DateTimeImmutable",
        },
    }

    def __init__(self):
        super().__init__("core/templates/php")

    def normalize_fields(self, fields: list):
        normalized = []
        imports = set()

        for field in fields:
            raw_type = field["type"]
            nullable = field.get("nullable", False)

            if raw_type not in self.TYPE_MAP:
                raise ValueError(f"Unsupported PHP type: {raw_type}")

            mapping = self.TYPE_MAP[raw_type]
            php_type = mapping["type"]

            if nullable:
                php_type = f"?{php_type}"

            normalized.append({
                "name": field["name"],
                "type": php_type,
            })

            if mapping["import"]:
                imports.add(mapping["import"])

        return normalized, sorted(imports)

    def generate(self, contract: dict, output_dir: str):
        template = self.load_template("dto.php.tpl")

        fields, imports = self.normalize_fields(contract["fields"])

        promoted_params = []
        modifier = "public readonly" if self.READONLY else "public"

        for field in fields:
            promoted_params.append(
                f"{modifier} {field['type']} ${field['name']}"
            )

        context = {
            "namespace": "App",
            "class_name": contract["entity"]["name"] + "Dto",
            "imports": imports,
            "promoted_params": promoted_params,
        }

        content = self.render(template, context)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / f"{context['class_name']}.php"
        file_path.write_text(content)

        return file_path
