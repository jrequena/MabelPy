from pathlib import Path

class BaseGenerator:
    def __init__(self, templates_path: str):
        self.templates_path = Path(templates_path)

    def load_template(self, name: str) -> str:
        path = self.templates_path / name
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        return path.read_text()

    def render(self, template: str, context: dict) -> str:
        output = template

        # Simple replacements
        for key, value in context.items():
            if isinstance(value, str):
                output = output.replace(f"{{{{ {key} }}}}", value)

        # Handle fields loop
        if "{% for field in fields %}" in output:
            before, rest = output.split("{% for field in fields %}")
            loop, after = rest.split("{% endfor %}")

            rendered = ""
            for field in context["fields"]:
                rendered += (
                    loop
                    .replace("{{ field.type }}", field["type"])
                    .replace("{{ field.name }}", field["name"])
                )

            output = before + rendered + after

        return output
