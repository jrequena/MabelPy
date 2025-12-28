from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpDtoGenerator(BaseGenerator):
    TYPE_MAP = {
        "int": {"type": "int", "import": None},
        "string": {"type": "string", "import": None},
        "bool": {"type": "bool", "import": None},
        "float": {"type": "float", "import": None},
        "datetime": {"type": "DateTimeImmutable", "import": "DateTimeImmutable"},
    }

    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config
        
        gen_config = config.get_generator_config("entity")
        self.READONLY = gen_config.get("immutable", True)
        self.ENABLE_VALIDATIONS = gen_config.get("validations", True)

    def generate(self, contract: dict, output_dir: Path):
        template = self.load_template("dto.php.tpl")
        
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        domain_suffix = self.config.get_generator_config("entity").get("namespace_suffix", "Domain")
        namespace = f"{base_ns}\\{domain_suffix.replace('/', '\\')}"
        
        fields, type_imports, enum_imports, vo_imports = self._normalize_fields(contract["fields"], namespace, contract.get("enums", {}))
        
        promoted_params = []
        use_readonly = self.READONLY and self.config.get("php.readonly_default", True)
        modifier = "public readonly" if use_readonly else "public"

        for field in fields:
            param = f"{modifier} {field['type']} ${field['name']}"
            if "default" in field and field["default"] is not None:
                if field.get("is_enum"):
                    param += " = " + self._format_enum_default(field["enum"], field["default"])
                else:
                    param += " = " + self._format_default(field["default"])
            elif field.get("nullable"):
                param += " = null"
                
            promoted_params.append(param)

        validations = self._generate_validations(contract["fields"])

        all_imports = sorted(list(set(type_imports)))
        if enum_imports:
            if all_imports: all_imports.append("")
            all_imports.extend(sorted(list(set(enum_imports))))
        if vo_imports:
            if all_imports: all_imports.append("")
            all_imports.extend(sorted(list(set(vo_imports))))

        imports_block = "\n".join([f"use {imp};" if imp else "" for imp in all_imports])
        if imports_block:
            imports_block += "\n"

        context = {
            "namespace": namespace,
            "class_name": entity_name,
            "imports_block": imports_block,
            "promoted_params": promoted_params,
            "validations": validations,
        }

        content = self.render(template, context)
        
        target_dir = output_dir / domain_suffix
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / f"{entity_name}.php"
        file_path.write_text(content)
        return file_path

    def _normalize_fields(self, fields: list, namespace: str, enums: dict):
        normalized = []
        type_imports = []
        enum_imports = []
        vo_imports = []
        
        auto_vos = self.config.get("generators.value_objects.auto_types", [])

        for field in fields:
            raw_type = field["type"]
            nullable = field.get("nullable", False)

            if raw_type == "enum":
                enum_name = field["enum"]
                php_type = f"?{enum_name}" if nullable else enum_name
                normalized.append({
                    "name": field["name"],
                    "type": php_type,
                    "is_enum": True,
                    "enum": enum_name,
                    "default": field.get("default"),
                    "nullable": nullable
                })
                enum_imports.append(f"{namespace}\\Enum\\{enum_name}")
                continue

            if raw_type in self.TYPE_MAP:
                mapping = self.TYPE_MAP[raw_type]
                php_type = f"?{mapping['type']}" if nullable else mapping["type"]
                normalized.append({
                    "name": field["name"],
                    "type": php_type,
                    "default": field.get("default"),
                    "nullable": nullable
                })
                if mapping["import"]:
                    type_imports.append(mapping["import"])
            elif raw_type in auto_vos:
                php_type = f"?{raw_type}" if nullable else raw_type
                normalized.append({
                    "name": field["name"],
                    "type": php_type,
                    "default": field.get("default"),
                    "nullable": nullable
                })
                vo_imports.append(f"{namespace}\\ValueObject\\{raw_type}")
            else:
                normalized.append({
                    "name": field["name"],
                    "type": raw_type,
                    "default": field.get("default"),
                    "nullable": nullable
                })

        return normalized, type_imports, enum_imports, vo_imports

    def _format_default(self, value):
        if value is None: return "null"
        if isinstance(value, bool): return "true" if value else "false"
        if isinstance(value, str): return f'"{value}"'
        return str(value)

    def _format_enum_default(self, enum_name: str, value: str):
        case = value.upper().replace('-', '_').replace(' ', '_')
        return f"{enum_name}::{case}"

    def _generate_validations(self, fields: list):
        validations = []
        for field in fields:
            name = field["name"]
            rules = field.get("validations", [])
            nullable = field.get("nullable", False)
            for rule in rules:
                if rule == "positive" and field["type"] == "int":
                    cond = f"${name} <= 0" if not nullable else f"${name} !== null && ${name} <= 0"
                    validations.append(f'if ({cond}) {{ throw new \\InvalidArgumentException("{name} must be positive"); }}')
                elif rule == "email" and field["type"] == "string":
                    cond = f"!filter_var(${name}, FILTER_VALIDATE_EMAIL)" if not nullable else f"${name} !== null && !filter_var(${name}, FILTER_VALIDATE_EMAIL)"
                    validations.append(f'if ({cond}) {{ throw new \\InvalidArgumentException("{name} must be a valid email"); }}')
        return validations
