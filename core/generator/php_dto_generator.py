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

            field_def = {
                "name": field["name"],
                "type": php_type,
            }

            # 👉 solo incluir default si viene definido
            if "default" in field:
                field_def["default"] = field["default"]

            # 👉 solo incluir validations si viene definido
            if "validations" in field:
                field_def["validations"] = field["validations"]

            normalized.append(field_def)

            if mapping["import"]:
                imports.add(mapping["import"])

        return normalized, sorted(imports)

    def generate(self, contract: dict, output_dir: str):
        template = self.load_template("dto.php.tpl")

        fields, imports = self.normalize_fields(contract["fields"])

        promoted_params = []
        modifier = "public readonly" if self.READONLY else "public"

        for field in fields:
            param = f"{modifier} {field['type']} ${field['name']}"

            if "default" in field:
                param += " = " + self.format_default(field["default"])

            promoted_params.append(param)

        validations = self.generate_validations(contract["fields"])

        context = {
            "namespace": "App",
            "class_name": contract["entity"]["name"] + "Dto",
            "imports": imports,
            "promoted_params": promoted_params,
            "validations": validations,
        }

        content = self.render(template, context)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / f"{context['class_name']}.php"
        file_path.write_text(content)

        return file_path

    def format_default(self, value):
        if value is None:
            return "null"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, str):
            return f'"{value}"'
        return str(value)

    def generate_validations(self, fields: list):
        """Genera líneas PHP de validación para el constructor."""
        validations = []

        for field in fields:
            name = field["name"]
            rules = field.get("validations", [])
            nullable = field.get("nullable", False)

            for rule in rules:
                if rule == "positive" and "int" in field["type"]:
                    indent = " " * 8  # 8 espacios = dos niveles en tu template
                    condition = f"${name} <= 0" if not nullable else f"${name} !== null && ${name} <= 0"
                    validations.append(
                        f"if ({condition}) {{\n{indent}    throw new \\InvalidArgumentException(\"{name} must be positive\");\n{indent}}}"
                    )
                elif rule == "email" and "string" in field["type"]:
                    indent = " " * 8  # 8 espacios = dos niveles en tu template
                    condition = f"!filter_var(${name}, FILTER_VALIDATE_EMAIL)" if not nullable else f"${name} !== null && !filter_var(${name}, FILTER_VALIDATE_EMAIL)"
                    validations.append(
                        f"if ({condition}) {{\n{indent}    throw new \\InvalidArgumentException(\"{name} must be a valid email\");\n{indent}}}"
                    )
                # Aquí puedes agregar más reglas (regex, minLength, maxLength, etc.)

        return validations




