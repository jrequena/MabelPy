from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpControllerGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        use_cases = contract.get("use_cases", {})
        if not use_cases:
            return []

        entities = list(contract.get("entities", {}).keys())
        primary_entity = entities[0] if entities else "Default"
        
        generated_files = []
        for uc_name, uc_def in use_cases.items():
            entity_name = uc_def.get("entity", primary_entity)
            generated_files.append(self._generate_controller(entity_name, uc_name, uc_def, output_dir))
            
        return generated_files

    def _generate_controller(self, entity_name: str, uc_name: str, uc_def: dict, output_dir: Path):
        base_ns = self.config.project_namespace
        
        # Controller target
        ctrl_suffix = "Infrastructure/Http/Controllers"
        target_ns = f"{base_ns}\\{ctrl_suffix.replace('/', '\\')}"
        target_dir = output_dir / ctrl_suffix
        target_dir.mkdir(parents=True, exist_ok=True)

        class_name = f"{uc_name}Controller"
        
        # Use Case info
        uc_config = self.config.get_generator_config("use_case")
        uc_ns_suffix = uc_config.get("namespace_suffix", "Domain/UseCase")
        use_case_ns = f"{base_ns}\\{uc_ns_suffix.replace('/', '\\')}\\{entity_name}\\{uc_name}"
        use_case_class = f"{uc_name}UseCase"
        use_case_request_class = f"{uc_name}Request"
        
        # Form Request info
        req_ns_suffix = "Infrastructure/Http/Requests"
        request_ns = f"{base_ns}\\{req_ns_suffix.replace('/', '\\')}"
        request_class = f"{uc_name}Request"
        
        inputs = uc_def.get("input", {})
        request_fields = [f.replace("?", "") for f in inputs.keys()]
        
        is_list = uc_name.startswith(("List", "GetAll", "Search"))
        if is_list:
            if "page" not in request_fields:
                request_fields.append("page")
            if "per_page" not in request_fields:
                request_fields.append("per_page")

        template = self.load_template("controller.php.tpl")
        context = {
            "namespace": target_ns,
            "class_name": class_name,
            "is_list": is_list,
            "request_class": request_class,
            "request_full_class": f"{request_ns}\\{request_class}",
            "use_case_class": use_case_class,
            "use_case_full_class": f"{use_case_ns}\\{use_case_class}",
            "use_case_request_class": use_case_request_class,
            "use_case_request_full_class": f"{use_case_ns}\\{use_case_request_class}",
            "request_fields": request_fields
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{class_name}.php"
        file_path.write_text(content)
        return file_path
