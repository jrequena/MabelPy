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

        for field in contract["fields"]:
            if "name" not in field or "type" not in field:
                raise ValueError("Each field must have name and type")
