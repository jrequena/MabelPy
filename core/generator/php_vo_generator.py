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
        if vo_type.lower() in ["id", "int"]:
            php_type = "int"
        
        validations = ""
        if vo_type.lower() == "email":
            validations = 'if (!filter_var($value, FILTER_VALIDATE_EMAIL)) {\n            throw new \\InvalidArgumentException("Invalid email format");\n        }'
        
        readonly = "readonly " if self.config.get("php.readonly_default", True) else ""
        
        context = {
            "namespace": namespace,
            "class_name": name,
            "readonly": readonly,
            "type": php_type,
            "validations": validations
        }
        
        content = self.render(template, context)
        
        # Use config paths
        vo_dir = output_dir / domain_suffix / "ValueObject"
        vo_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = vo_dir / f"{name}.php"
        file_path.write_text(content)
        
        return file_path
