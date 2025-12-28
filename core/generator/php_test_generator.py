from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpTestGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        template = self.load_template("test_entity.php.tpl")
        
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        
        test_config = self.config.get_generator_config("tests")
        test_suffix = test_config.get("namespace_suffix", "Tests")
        namespace = f"{base_ns}\\{test_suffix.replace('/', '\\')}"
        
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        entity_ns = f"{base_ns}\\{domain_suffix.replace('/', '\\')}"
        
        fields_data = self._prepare_fields(contract["fields"], entity_ns, contract.get("enums", {}))
        
        imports = [f"{entity_ns}\\{entity_name}"]
        for f in fields_data:
            if f.get("import"):
                imports.append(f["import"])

        imports_block = "\n".join([f"use {imp};" for imp in sorted(list(set(imports)))])
        if imports_block:
            imports_block += "\n"

        context = {
            "namespace": namespace,
            "class_name": entity_name,
            "imports_block": imports_block,
            "fields": fields_data
        }
        
        content = self.render(template, context)
        
        # Test directory usually outside src, but mabel.yaml says 'tests'
        # Let's use the path from mabel.yaml
        test_root = Path(self.config.get("paths.tests", "tests")).absolute()
        target_dir = test_root / entity_name
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / f"{entity_name}Test.php"
        file_path.write_text(content)
        return file_path

    def _prepare_fields(self, fields: list, domain_ns: str, enums: dict):
        prepared = []
        auto_vos = self.config.get("generators.value_objects.auto_types", [])
        
        for field in fields:
            name = field["name"]
            raw_type = field["type"]
            
            f_data = {
                "name": name,
                "import": None
            }

            if raw_type == "enum":
                enum_name = field["enum"]
                f_data["import"] = f"{domain_ns}\\Enum\\{enum_name}"
                f_data["sample_value"] = f"{enum_name}::ACTIVE"
            
            elif raw_type in auto_vos:
                f_data["import"] = f"{domain_ns}\\ValueObject\\{raw_type}"
                if raw_type == "Email":
                    f_data["sample_value"] = f"new Email('test@example.com')"
                else:
                    f_data["sample_value"] = f"new {raw_type}('sample')"
            
            elif raw_type == "datetime":
                f_data["sample_value"] = f"new \\DateTimeImmutable()"
            
            elif raw_type == "int":
                f_data["sample_value"] = "1"
            elif raw_type == "string":
                f_data["sample_value"] = "'sample'"
            elif raw_type == "bool":
                f_data["sample_value"] = "true"
            else:
                f_data["sample_value"] = "null"
                
            prepared.append(f_data)
            
        return prepared
