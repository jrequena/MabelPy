from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpMapperGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        template = self.load_template("mapper.php.tpl")
        
        entity_name = contract["entity"]["name"]
        base_ns = self.config.project_namespace
        
        mapper_config = self.config.get_generator_config("mapper")
        mapper_suffix = mapper_config.get("namespace_suffix", "Infrastructure/Mapper")
        namespace = f"{base_ns}\\{mapper_suffix.replace('/', '\\')}"
        
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
            "class_name": f"{entity_name}Mapper",
            "entity_name": entity_name,
            "imports_block": imports_block,
            "fields": fields_data
        }
        
        # BaseGenerator expects some keys for legacy loop emulation if still used
        for f in fields_data:
             f["name"] = f["raw_name"]

        content = self.render(template, context)
        
        target_dir = output_dir / mapper_suffix
        target_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = target_dir / f"{entity_name}Mapper.php"
        file_path.write_text(content)
        return file_path

    def _prepare_fields(self, fields: list, domain_ns: str, enums: dict):
        prepared = []
        auto_vos = self.config.get("generators.value_objects.auto_types", [])
        
        for field in fields:
            name = field["name"]
            raw_type = field.get("type")
            nullable = field.get("nullable", False)
            
            f_data = {
                "raw_name": name,
                "import": None
            }

            # Handle Relationships
            if "has_many" in field:
                 f_data["from_array_line"] = f"[] // TODO: Map collection {field['has_many']}"
                 f_data["to_array_line"] = f"[] // TODO: Map collection {field['has_many']}"
                 prepared.append(f_data)
                 continue

            if "belongs_to" in field or "has_one" in field:
                 target = field.get("belongs_to") or field.get("has_one")
                 f_data["from_array_line"] = f"null // TODO: Map relation {target}"
                 f_data["to_array_line"] = f"null // TODO: Map relation {target}"
                 prepared.append(f_data)
                 continue

            if not raw_type: continue

            if raw_type == "enum" or raw_type in enums:
                enum_name = field.get("enum") or raw_type
                f_data["import"] = f"{domain_ns}\\Enum\\{enum_name}"
                if nullable:
                    f_data["from_array_line"] = f"isset($data['{name}']) ? {enum_name}::from($data['{name}']) : null"
                    f_data["to_array_line"] = f"$entity->{name}?->value"
                else:
                    f_data["from_array_line"] = f"{enum_name}::from($data['{name}'])"
                    f_data["to_array_line"] = f"$entity->{name}->value"
            
            elif raw_type in auto_vos:
                f_data["import"] = f"{domain_ns}\\ValueObject\\{raw_type}"
                if nullable:
                    f_data["from_array_line"] = f"isset($data['{name}']) ? new {raw_type}($data['{name}']) : null"
                    f_data["to_array_line"] = f"$entity->{name}?->value"
                else:
                    f_data["from_array_line"] = f"new {raw_type}($data['{name}'])"
                    f_data["to_array_line"] = f"$entity->{name}->value"
            
            elif raw_type == "datetime":
                if nullable:
                    f_data["from_array_line"] = f"isset($data['{name}']) ? new \\DateTimeImmutable($data['{name}']) : null"
                    f_data["to_array_line"] = f"$entity->{name}?->format(\\DateTimeInterface::ATOM)"
                else:
                    f_data["from_array_line"] = f"new \\DateTimeImmutable($data['{name}'])"
                    f_data["to_array_line"] = f"$entity->{name}->format(\\DateTimeInterface::ATOM)"
            
            else:
                f_data["from_array_line"] = f"$data['{name}'] ?? null"
                f_data["to_array_line"] = f"$entity->{name}"
                
            prepared.append(f_data)
            
        return prepared
