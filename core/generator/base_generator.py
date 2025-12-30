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

    def add_filter(self, name: str, func):
        self.env.filters[name] = func

    def render(self, template, context: dict) -> str:
        if isinstance(template, str):
            content = self.env.from_string(template).render(**context)
        else:
            content = template.render(**context)
        
        return content.rstrip() + "\n"
