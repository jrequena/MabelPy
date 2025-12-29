from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpUseCaseGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        use_cases = contract.get("use_cases", {})
        if not use_cases:
            return []

        # In UserMVP.yaml, use cases are top-level. 
        # We'll associate them with the first entity if not specified.
        entities = list(contract.get("entities", {}).keys())
        primary_entity = entities[0] if entities else "Default"

        generated_files = []
        for uc_name, uc_def in use_cases.items():
            # Try to find target entity in uc_def or use primary
            entity_name = uc_def.get("entity", primary_entity)
            generated_files.extend(self._generate_single_use_case(entity_name, uc_name, uc_def, output_dir))
            
        return generated_files

    def _generate_single_use_case(self, entity_name: str, uc_name: str, uc_def: dict, output_dir: Path):
        files = []
        base_ns = self.config.project_namespace
        
        uc_config = self.config.get_generator_config("use_case")
        uc_suffix = uc_config.get("namespace_suffix", "Domain/UseCase")
        
        target_ns = f"{base_ns}\\{uc_suffix.replace('/', '\\')}\\{entity_name}\\{uc_name}"
        target_dir = output_dir / uc_suffix / entity_name / uc_name
        target_dir.mkdir(parents=True, exist_ok=True)

        req_class = f"{uc_name}Request"
        res_class = f"{uc_name}Response"

        # Generate Request/Response DTOs if enabled
        if uc_config.get("with_request_response", True):
            inputs = uc_def.get("input", {})
            if isinstance(inputs, dict):
                files.append(self._generate_dto(target_ns, req_class, inputs, target_dir))
            
            output = uc_def.get("output", "void")
            # If output is a string (entity name or primitive), we create a response with one field or use it directly
            # For simplicity in MVP, we create a response DTO if it's a mapping or just a simple one.
            res_fields = {}
            if isinstance(output, dict):
                res_fields = output
            elif isinstance(output, str) and output != "void":
                res_fields = {"data": output}
            
            files.append(self._generate_dto(target_ns, res_class, res_fields, target_dir))

        # Generate UseCase
        template = self.load_template("use_case.php.tpl")
        
        repo_config = self.config.get_generator_config("repository")
        repo_suffix = repo_config.get("interface_namespace_suffix", "Domain/Repository")
        repo_ns = f"{base_ns}\\{repo_suffix.replace('/', '\\')}"
        repo_name = f"{entity_name}Repository"
        
        context = {
            "namespace": target_ns,
            "class_name": f"{uc_name}UseCase",
            "repository_name": repo_name,
            "request_class": req_class,
            "response_class": res_class,
            "imports_block": f"use {repo_ns}\\{repo_name};"
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{uc_name}UseCase.php"
        file_path.write_text(content)
        files.append(file_path)
        
        return files

    def _generate_dto(self, namespace: str, class_name: str, fields: dict, target_dir: Path):
        template = self.load_template("use_case_dto.php.tpl")
        
        promoted_params = []
        for f_name, f_def in fields.items():
            f_type = f_def if isinstance(f_def, str) else f_def.get("type", "mixed")
            # Remove optional marker if present
            f_type = f_type.replace("?", "")
            f_name = f_name.replace("?", "")
            promoted_params.append(f"public readonly {f_type} ${f_name}")
            
        context = {
            "namespace": namespace,
            "class_name": class_name,
            "promoted_params": promoted_params
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{class_name}.php"
        file_path.write_text(content)
        return file_path
