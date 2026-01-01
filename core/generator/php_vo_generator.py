from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpValueObjectGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, name: str, vo_type: str, output_dir: Path):
        template = self.load_template("value_object.php.tpl")
        
        # Determine namespace: Base + Domain + ValueObject (optional)
        base_ns = self.config.project_namespace
        domain_suffix = self.config.get_generator_config("value_objects").get("namespace_suffix", "Domain")
        namespace = f"{base_ns}\\{domain_suffix.replace('/', '\\')}\\ValueObject"
        
        # PHP Type mapping
        php_type = "string"
        vo_type_lower = vo_type.lower()
        
        if vo_type_lower in ["id", "int", "integer"]:
            php_type = "int"
        elif vo_type_lower in ["float", "double", "decimal"]:
            php_type = "float"
        elif vo_type_lower in ["bool", "boolean"]:
            php_type = "bool"
        
        validations = []
        if vo_type_lower == "email":
            validations.append('if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {\n    throw new \\InvalidArgumentException("Invalid email format");\n}')
        elif vo_type_lower == "uuid":
            validations.append('if (!preg_match("/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i", $value)) {\n    throw new \\InvalidArgumentException("Invalid UUID format");\n}')
        elif vo_type_lower == "url":
            validations.append('if (!filter_var($value, FILTER_VALIDATE_URL)) {\n    throw new \\InvalidArgumentException("Invalid URL format");\n}')
        elif vo_type_lower == "positive_int":
            php_type = "int"
            validations.append('if ($value <= 0) {\n    throw new \\InvalidArgumentException("Value must be a positive integer");\n}')
        
        readonly = "readonly " if self.config.get("php.readonly_default", True) else ""
        
        context = {
            "namespace": namespace,
            "class_name": name,
            "readonly": readonly,
            "type": php_type,
            "validations": "\n".join(validations)
        }
        
        content = self.render(template, context)
        
        # Use config paths
        vo_dir = output_dir / domain_suffix / "ValueObject"
        vo_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = vo_dir / f"{name}.php"
        file_path.write_text(content)
        
        return file_path
