from pathlib import Path
from core.generator.base_generator import BaseGenerator

class PhpEnumGenerator(BaseGenerator):
    def __init__(self, config: dict):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, name: str, enum_def: dict, output_dir: str):
        template = self.load_template("enum.php.tpl")

        if "type" not in enum_def or enum_def["type"] != "string":
            raise ValueError("Currently only string backed enums are supported")

        values = enum_def.get("values", [])
        if not isinstance(values, list) or not values:
            raise ValueError("Enum must define a non-empty 'values' list")

        namespace = self.config.get("namespace", "App")

        # Prepare values context: case name uppercase safe
        values_ctx = []
        for v in values:
            case = v.upper().replace('-', '_').replace(' ', '_')
            values_ctx.append({"value": v, "case": case})

        context = {
            "namespace": namespace,
            "enum_name": name,
            "values": values_ctx,
        }

        content = self.render(template, context)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / f"{name}.php"
        file_path.write_text(content)

        return file_path