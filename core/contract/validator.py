import re
from typing import Any, Dict


class ContractValidator:
    PRIMITIVE_TYPES = {"int", "string", "float", "bool", "datetime", "Email", "Id", "Uuid"}

    def validate(self, contract: Dict[str, Any]):
        if not isinstance(contract, dict):
            raise ValueError("Contract must be a mapping/dictionary")

        # Module (optional)
        module = contract.get("module")
        if module is not None:
            if not isinstance(module, dict):
                raise ValueError("'module' must be a mapping with 'name' and 'namespace'")
            if "name" not in module or "namespace" not in module:
                raise ValueError("'module' must include 'name' and 'namespace'")

        # Enums
        enums = contract.get("enums", {})
        if enums is not None:
            if not isinstance(enums, dict):
                raise ValueError("'enums' must be a mapping of name -> definition")
            for name, enum_def in enums.items():
                if not isinstance(enum_def, dict):
                    raise ValueError(f"Enum '{name}' must be a mapping")
                if enum_def.get("type") != "string":
                    raise ValueError(f"Enum '{name}' must define type: string")
                values = enum_def.get("values")
                if not isinstance(values, list) or not values:
                    raise ValueError(f"Enum '{name}' must define a non-empty 'values' list")
                for v in values:
                    if not isinstance(v, str) or not v:
                        raise ValueError(f"Enum '{name}' has an invalid value: {v}")

        # Entities
        entities = contract.get("entities")
        if entities is None:
             raise ValueError("Contract must define 'entities' as a mapping of name -> fields")

        for entity_name, fields in entities.items():
            if not isinstance(fields, dict):
                raise ValueError(f"Entity '{entity_name}' must define fields as a mapping")
            for field_name, field_def in fields.items():
                if isinstance(field_def, str):
                    self._validate_type_reference(field_def, enums, entities, entity_name, field_name)
                elif isinstance(field_def, dict):
                    # Check for relationship
                    rel_type = None
                    if "belongs_to" in field_def:
                        rel_type = "belongs_to"
                    elif "has_many" in field_def:
                        rel_type = "has_many"
                    elif "has_one" in field_def:
                        rel_type = "has_one"
                    
                    if rel_type:
                        target = field_def[rel_type]
                        if target not in entities:
                            raise ValueError(f"Relationship '{rel_type}' in '{entity_name}.{field_name}' references unknown entity '{target}'")
                        continue

                    if "type" not in field_def:
                        raise ValueError(f"Field '{field_name}' in '{entity_name}' must specify 'type'")
                    ftype = field_def["type"]
                    if ftype == "enum":
                        enum_name = field_def.get("enum")
                        if not enum_name or enum_name not in enums:
                            raise ValueError(f"Field '{field_name}' references undefined enum '{enum_name}'")
                    else:
                        self._validate_type_reference(ftype, enums, entities, entity_name, field_name)
                    self._validate_constraints(field_def, entity_name, field_name)
                else:
                    raise ValueError(f"Invalid definition for field '{field_name}' in '{entity_name}'")

        # Use cases
        use_cases = contract.get("use_cases", {})
        if use_cases is not None:
            if not isinstance(use_cases, dict):
                raise ValueError("'use_cases' must be a mapping of name -> definition")
            for uc_name, uc_def in use_cases.items():
                if not isinstance(uc_def, dict):
                    raise ValueError(f"Use case '{uc_name}' must be a mapping")
                
                inputs = uc_def.get("input", {})
                if not isinstance(inputs, dict):
                    raise ValueError(f"Use case '{uc_name}' input must be a mapping")
                for in_name, in_type in inputs.items():
                    if isinstance(in_type, str):
                        self._validate_type_reference(in_type.replace("?", ""), enums, entities, f"use_case:{uc_name}", in_name)
                    else:
                        raise ValueError(f"Invalid input type for '{in_name}' in use case '{uc_name}'")

                output = uc_def.get("output")
                if output:
                    if isinstance(output, str):
                        clean_output = output.replace("?", "")
                        if clean_output != "void":
                            self._validate_type_reference(clean_output, enums, entities, f"use_case:{uc_name}", "output")
                    elif isinstance(output, dict):
                        for out_name, out_type in output.items():
                            if isinstance(out_type, str):
                                self._validate_type_reference(out_type.replace("?", ""), enums, entities, f"use_case:{uc_name}:output", out_name)
                    else:
                        raise ValueError(f"Invalid output definition for use case '{uc_name}'")

                rules = uc_def.get("rules", [])
                if not isinstance(rules, list):
                    raise ValueError(f"Rules for use case '{uc_name}' must be a list")
                for rule in rules:
                    if not isinstance(rule, dict) or len(rule) != 1:
                        raise ValueError(f"Each rule in '{uc_name}' must be a single-key mapping (e.g., ensure: condition)")
                    rule_type = list(rule.keys())[0]
                    if rule_type not in {"ensure", "set_default", "transition", "emit"}:
                        raise ValueError(f"Unknown rule type '{rule_type}' in use case '{uc_name}'")

    def _validate_type_reference(self, type_name: str, enums: Dict[str, Any], entities: Dict[str, Any], ctx_entity: str, ctx_field: str):
        if type_name in self.PRIMITIVE_TYPES:
            return
        if type_name in enums:
            return
        if type_name in entities:
            return
        raise ValueError(f"Unknown type referenced for '{ctx_field}' in '{ctx_entity}': {type_name}")

    def _validate_constraints(self, field_def: Dict[str, Any], entity_name: str, field_name: str):
        if "min" in field_def and not isinstance(field_def["min"], (int, float)):
            raise ValueError(f"Constraint 'min' for '{field_name}' in '{entity_name}' must be numeric")
        if "max" in field_def and not isinstance(field_def["max"], (int, float)):
            raise ValueError(f"Constraint 'max' for '{field_name}' in '{entity_name}' must be numeric")
        if "length" in field_def and not isinstance(field_def["length"], int):
            raise ValueError(f"Constraint 'length' for '{field_name}' in '{entity_name}' must be integer")
        if "regex" in field_def:
            try:
                re.compile(field_def["regex"])
            except Exception:
                raise ValueError(f"Constraint 'regex' for '{field_name}' in '{entity_name}' is not a valid regex")
