class ContractValidator:
    def validate(self, contract: dict):
        if "entity" not in contract:
            raise ValueError("Contract must define 'entity'")

        if "name" not in contract["entity"]:
            raise ValueError("Entity must have a name")

        if "fields" not in contract:
            raise ValueError("Contract must define fields")

        if not isinstance(contract["fields"], list):
            raise ValueError("Fields must be a list")

        # Optional: validate enums structure
        if "enums" in contract:
            if not isinstance(contract["enums"], dict):
                raise ValueError("Enums must be a mapping of name -> definition")
            for name, enum_def in contract["enums"].items():
                if not isinstance(enum_def, dict):
                    raise ValueError(f"Enum '{name}' must be a mapping")
                if "type" not in enum_def or enum_def["type"] != "string":
                    raise ValueError(f"Enum '{name}' must define type: string")
                if "values" not in enum_def or not isinstance(enum_def["values"], list) or not enum_def["values"]:
                    raise ValueError(f"Enum '{name}' must define a non-empty 'values' list")

        for field in contract["fields"]:
            if "name" not in field or "type" not in field:
                raise ValueError("Each field must have name and type")

            if field["type"] == "enum":
                if "enum" not in field:
                    raise ValueError("Enum fields must specify the 'enum' name")
                if "enums" not in contract or field["enum"] not in contract["enums"]:
                    raise ValueError(f"Field '{field.get('name')}' references undefined enum '{field.get('enum')}'")
