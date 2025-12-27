from pathlib import Path

class BaseGenerator:
    def __init__(self, templates_path: str):
        self.templates_path = Path(templates_path)

    def load_template(self, name: str) -> str:
        path = self.templates_path / name
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        return path.read_text()

    def _render_loop(self, template: str, loop_name: str, items, render_item):
        start_tag = f"{{% for {loop_name} in {loop_name}s %}}"
        end_tag = "{% endfor %}"

        if start_tag not in template:
            return template

        before, rest = template.split(start_tag, 1)
        loop_block, after = rest.split(end_tag, 1)

        rendered = ""
        for item in items:
            rendered += render_item(loop_block, item)

        # If loop had no items, avoid leaving extra blank lines from the template block
        if rendered == "":
            # remove one adjacent newline if both sides have one to prevent double blank lines
            if before.endswith('\n') and after.startswith('\n'):
                before = before.rstrip('\n') + '\n'
            return before + after

        return before + rendered + after

    def render(self, template: str, context: dict) -> str:
        output = template

        # Simple replacements
        for key, value in context.items():
            if isinstance(value, str):
                output = output.replace(f"{{{{ {key} }}}}", value)

        # Imports loop
        output = self._render_loop(
            output,
            "import",
            context.get("imports", []),
            lambda block, imp: block.replace("{{ import }}", imp)
        )

        # Fields loop
        output = self._render_loop(
            output,
            "field",
            context.get("fields", []),
            lambda block, field: (
                block
                .replace("{{ field.type }}", field["type"])
                .replace("{{ field.name }}", field["name"])
            )
        )

        # Promoted params loop
        output = self._render_loop(
            output,
            "promoted_param",
            context.get("promoted_params", []),
            lambda block, param: block.replace("{{ promoted_param }}", param)
        )

        # ✅ Nuevo loop para validaciones
        output = self._render_loop(
            output,
            "validation",
            context.get("validations", []),
            lambda block, line: block.replace("{{ validation }}", line)
        )

        # ✅ Nuevo loop para enum values ({{ value }} y {{ case }})
        output = self._render_loop(
            output,
            "value",
            context.get("values", []),
            lambda block, value: block.replace("{{ value }}", value["value"]).replace("{{ case }}", value["case"]) 
        )

        # Reemplazo de variables simples
        for key, value in context.items():
            if not isinstance(value, list):
                output = output.replace(f"{{{{ {key} }}}}", str(value))

        # Normalizar saltos de línea múltiples a máximo dos para evitar líneas en blanco extra
        import re
        output = re.sub(r"\n{3,}", "\n\n", output)

        return output
