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

        parts = template.split(start_tag)
        new_template = parts[0]
        
        for part in parts[1:]:
            if end_tag not in part:
                new_template += start_tag + part
                continue
                
            loop_block, rest = part.split(end_tag, 1)
            
            rendered = ""
            for item in items:
                rendered += render_item(loop_block, item)
            
            if rendered == "" and new_template.endswith('\n') and rest.startswith('\n'):
                 new_template = new_template.rstrip('\n') + '\n'
                 rest = rest.lstrip('\n')
                 
            new_template += rendered + rest
            
        return new_template

    def render(self, template: str, context: dict) -> str:
        output = template

        for key, value in context.items():
            if isinstance(value, str):
                output = output.replace(f"{{{{ {key} }}}}", value)

        for loop_name in ["import", "field", "promoted_param", "validation", "value"]:
            items = context.get(f"{loop_name}s", [])
            if loop_name == "field":
                output = self._render_loop(
                    output,
                    "field",
                    items,
                    lambda block, field: (
                        block
                        .replace("{{ field.type }}", str(field.get("type", "")))
                        .replace("{{ field.name }}", str(field.get("name", "")))
                        .replace("{{ field.from_array_line }}", str(field.get("from_array_line", "")))
                        .replace("{{ field.to_array_line }}", str(field.get("to_array_line", "")))
                        .replace("{{ field.raw_name }}", str(field.get("raw_name", "")))
                        .replace("{{ field.sample_value }}", str(field.get("sample_value", "")))
                    )
                )
            elif loop_name == "import":
                output = self._render_loop(
                    output, "import", items,
                    lambda block, imp: block.replace("{{ import }}", str(imp))
                )
            elif loop_name == "promoted_param":
                output = self._render_loop(
                    output, "promoted_param", items,
                    lambda block, param: block.replace("{{ promoted_param }}", str(param))
                )
            elif loop_name == "validation":
                output = self._render_loop(
                    output, "validation", items,
                    lambda block, line: block.replace("{{ validation }}", str(line))
                )
            elif loop_name == "value":
                output = self._render_loop(
                    output, "value", items,
                    lambda block, value: block.replace("{{ value }}", str(value["value"])).replace("{{ case }}", str(value["case"]))
                )

        for key, value in context.items():
            if not isinstance(value, list):
                output = output.replace(f"{{{{ {key} }}}}", str(value))

        return output
