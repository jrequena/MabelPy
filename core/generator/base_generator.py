from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

class BaseGenerator:
    def __init__(self, templates_path: str):
        self.templates_path = Path(templates_path)
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_path)),
            autoescape=select_autoescape(),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def load_template(self, name: str):
        return self.env.get_template(name)

    def render(self, template, context: dict) -> str:
        # For backward compatibility, if template is a string, we might need to handle it.
        # But load_template now returns a Jinja template object.
        if isinstance(template, str):
            # If it's already a string, we can use a temporary template
            return self.env.from_string(template).render(**context)
        return template.render(**context)
