from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpUseCaseGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        entity_name = contract["entity"]["name"]
        use_cases = contract.get("use_cases", {})
        
        if not use_cases:
            return []

        generated_files = []
        for uc_name, uc_def in use_cases.items():
            generated_files.extend(self._generate_single_use_case(entity_name, uc_name, uc_def, output_dir))
            
        return generated_files

    def _generate_single_use_case(self, entity_name: str, uc_name: str, uc_def: dict, output_dir: Path):
        files = []
        base_ns = self.config.project_namespace
        
        uc_config = self.config.get_generator_config("use_case")
        uc_suffix = uc_config.get("namespace_suffix", "Domain/UseCase")
        
        # Folder structure: src/Domain/UseCase/User/FetchUser
        # We'll put Request/Response in the same folder as the UseCase
        target_ns = f"{base_ns}\\{uc_suffix.replace('/', '\\')}\\{entity_name}\\{uc_name}"
        target_dir = output_dir / uc_suffix / entity_name / uc_name
        target_dir.mkdir(parents=True, exist_ok=True)

        req_class = f"{uc_name}Request"
        res_class = f"{uc_name}Response"

        # Generate Request/Response DTOs if enabled
        if uc_config.get("with_request_response", True):
            files.append(self._generate_dto(target_ns, req_class, uc_def.get("input", {}), target_dir))
            files.append(self._generate_dto(target_ns, res_class, uc_def.get("output", {}), target_dir))

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
        for f_name, f_type in fields.items():
            promoted_params.append(f"{f_type} ${f_name}")
            
        context = {
            "namespace": namespace,
            "class_name": class_name,
            "promoted_params": promoted_params
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{class_name}.php"
        file_path.write_text(content)
        return file_path
