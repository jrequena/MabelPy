from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpTestGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        self._generate_entity_test(contract)
        self._generate_vo_tests(contract)
        self._generate_mapper_test(contract)
        self._generate_use_case_tests(contract)

    def _generate_entity_test(self, contract: dict):
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
        imports_block = "\n".join([f"use {imp};" for imp in sorted(list(set(imports))) if imp])
        if imports_block:
            imports_block += "\n"
        context = {
            "namespace": namespace,
            "class_name": entity_name,
            "imports_block": imports_block,
            "fields": fields_data
        }
        content = self.render(template, context)
        self._write_test_file(entity_name, f"{entity_name}Test.php", content)

    def _generate_vo_tests(self, contract: dict):
        template = self.load_template("test_vo.php.tpl")
        base_ns = self.config.project_namespace
        test_suffix = self.config.get_generator_config("tests").get("namespace_suffix", "Tests")
        namespace = f"{base_ns}\\{test_suffix.replace('/', '\\')}"
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        vo_ns = f"{base_ns}\\{domain_suffix.replace('/', '\\')}\\ValueObject"
        auto_types = self.config.get("generators.value_objects.auto_types", [])
        generated_vos = set()
        for field in contract.get("fields", []):
            vo_name = field.get("type")
            if vo_name and vo_name in auto_types and vo_name not in generated_vos:
                sample_value = "'sample'"
                if vo_name == "Email":
                    sample_value = "'test@example.com'"
                elif vo_name in ["Id", "Uuid"]:
                    sample_value = "'123e4567-e89b-12d3-a456-426614174000'"
                context = {
                    "namespace": namespace,
                    "class_name": vo_name,
                    "vo_import": f"{vo_ns}\\{vo_name}",
                    "sample_value": sample_value
                }
                content = self.render(template, context)
                self._write_test_file(contract["entity"]["name"], f"{vo_name}Test.php", content)
                generated_vos.add(vo_name)

    def _generate_mapper_test(self, contract: dict):
        template = self.load_template("test_mapper.php.tpl")
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        test_suffix = self.config.get_generator_config("tests").get("namespace_suffix", "Tests")
        namespace = f"{base_ns}\\{test_suffix.replace('/', '\\')}"
        mapper_suffix = self.config.get_generator_config("mapper").get("namespace_suffix", "Infrastructure/Mapper")
        mapper_ns = f"{base_ns}\\{mapper_suffix.replace('/', '\\')}"
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        entity_ns = f"{base_ns}\\{domain_suffix.replace('/', '\\')}"
        fields_data = self._prepare_fields_for_mapper(contract["fields"], entity_ns)
        imports = [f"{entity_ns}\\{entity_name}", f"{mapper_ns}\\{entity_name}Mapper"]
        for f in fields_data:
            if f.get("import"):
                imports.append(f["import"])
        imports_block = "\n".join([f"use {imp};" for imp in sorted(list(set(imports))) if imp])
        if imports_block:
            imports_block += "\n"
        context = {
            "namespace": namespace,
            "class_name": f"{entity_name}Mapper",
            "entity_name": entity_name,
            "imports_block": imports_block,
            "fields": fields_data
        }
        content = self.render(template, context)
        self._write_test_file(entity_name, f"{entity_name}MapperTest.php", content)

    def _generate_use_case_tests(self, contract: dict):
        template = self.load_template("test_use_case.php.tpl")
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        test_suffix = self.config.get_generator_config("tests").get("namespace_suffix", "Tests")
        namespace = f"{base_ns}\\{test_suffix.replace('/', '\\')}"
        
        use_case_config = self.config.get_generator_config("use_case")
        use_case_suffix = use_case_config.get("namespace_suffix", "Domain/UseCase")
        
        repo_suffix = self.config.get_generator_config("repository").get("interface_namespace_suffix", "Domain/Repository")
        repo_ns = f"{base_ns}\\{repo_suffix.replace('/', '\\')}"
        
        use_cases = contract.get("use_cases", {})
        
        for uc_name in use_cases.keys():
            full_class_name = f"{uc_name}UseCase"
            # New structure: App\Domain\UseCase\{Entity}\{UseCaseName}\{UseCaseName}UseCase
            use_case_ns = f"{base_ns}\\{use_case_suffix.replace('/', '\\')}\\{entity_name}\\{uc_name}"
            
            imports = [
                f"{use_case_ns}\\{full_class_name}", 
                f"{repo_ns}\\{entity_name}Repository"
            ]
            imports_block = "\n".join([f"use {imp};" for imp in sorted(list(set(imports)))])
            if imports_block:
                imports_block += "\n"
                
            context = {
                "namespace": namespace,
                "class_name": full_class_name,
                "repository_name": f"{entity_name}Repository",
                "imports_block": imports_block
            }
            content = self.render(template, context)
            self._write_test_file(entity_name, f"{full_class_name}Test.php", content)

    def _write_test_file(self, entity_name: str, filename: str, content: str):
        test_root = Path(self.config.get("paths.tests", "tests")).absolute()
        target_dir = test_root / entity_name
        target_dir.mkdir(parents=True, exist_ok=True)
        file_path = target_dir / filename
        file_path.write_text(content)

    def _prepare_fields_for_mapper(self, fields: list, domain_ns: str):
        prepared = []
        auto_vos = self.config.get("generators.value_objects.auto_types", [])
        for field in fields:
            name = field["name"]
            raw_type = field.get("type")
            f_data = {"raw_name": name, "import": None}
            if "has_many" in field:
                f_data["sample_value"] = "[]"
                f_data["sample_raw_value"] = "[]"
            elif "belongs_to" in field or "has_one" in field:
                f_data["sample_value"] = "null"
                f_data["sample_raw_value"] = "null"
            elif raw_type == "enum":
                enum_name = field.get("enum") or raw_type
                f_data["import"] = f"{domain_ns}\\Enum\\{enum_name}"
                f_data["sample_value"] = f"{enum_name}::ACTIVE"
                f_data["sample_raw_value"] = "'ACTIVE'"
            elif raw_type in auto_vos:
                f_data["import"] = f"{domain_ns}\\ValueObject\\{raw_type}"
                val = "'test@example.com'" if raw_type == "Email" else "'sample'"
                f_data["sample_value"] = f"new {raw_type}({val})"
                f_data["sample_raw_value"] = val
            elif raw_type == "datetime":
                f_data["sample_value"] = "new \\DateTimeImmutable('2023-01-01 00:00:00')"
                f_data["sample_raw_value"] = "'2023-01-01T00:00:00+00:00'"
            elif raw_type == "int":
                f_data["sample_value"] = "1"
                f_data["sample_raw_value"] = "1"
            elif raw_type == "string":
                f_data["sample_value"] = "'sample'"
                f_data["sample_raw_value"] = "'sample'"
            elif raw_type == "bool":
                f_data["sample_value"] = "true"
                f_data["sample_raw_value"] = "true"
            else:
                f_data["sample_value"] = "null"
                f_data["sample_raw_value"] = "null"
            prepared.append(f_data)
        return prepared

    def _prepare_fields(self, fields: list, domain_ns: str, enums: dict):
        prepared = []
        auto_vos = self.config.get("generators.value_objects.auto_types", [])
        for field in fields:
            name = field["name"]
            raw_type = field.get("type")
            f_data = {"name": name, "import": None}
            if "has_many" in field:
                f_data["sample_value"] = "[]"
            elif "belongs_to" in field or "has_one" in field:
                f_data["sample_value"] = "null"
            elif raw_type == "enum":
                enum_name = field.get("enum") or raw_type
                f_data["import"] = f"{domain_ns}\\Enum\\{enum_name}"
                f_data["sample_value"] = f"{enum_name}::ACTIVE"
            elif raw_type in auto_vos:
                f_data["import"] = f"{domain_ns}\\ValueObject\\{raw_type}"
                val = "'test@example.com'" if raw_type == "Email" else "'sample'"
                f_data["sample_value"] = f"new {raw_type}({val})"
            elif raw_type == "datetime":
                f_data["sample_value"] = "new \\DateTimeImmutable()"
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
