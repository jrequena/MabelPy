from typing import Any, Dict, List


class ConfigValidator:
    REQUIRED_SECTIONS = ["project", "paths", "generators"]
    
    @classmethod
    def validate(cls, config: Dict[str, Any]) -> List[str]:
        errors = []
        
        # Check required sections
        for section in cls.REQUIRED_SECTIONS:
            if section not in config:
                errors.append(f"Missing required section: '{section}'")
                continue
            if not isinstance(config[section], dict):
                errors.append(f"Section '{section}' must be a mapping")

        if errors:
            return errors

        # Validate Project
        project = config["project"]
        for field in ["name", "namespace", "framework"]:
            if field not in project or not project[field]:
                errors.append(f"Project section missing required field: '{field}'")
        
        # Validate Framework
        valid_frameworks = ["zend", "symfony", "laravel"]
        if project.get("framework") and project["framework"].lower() not in valid_frameworks:
            errors.append(f"Invalid framework '{project['framework']}'. Valid options: {', '.join(valid_frameworks)}")

        # Validate Paths
        paths = config["paths"]
        required_paths = ["source_root", "domain", "application", "infrastructure", "tests"]
        for path_key in required_paths:
            if path_key not in paths or not paths[path_key]:
                errors.append(f"Paths section missing required field: '{path_key}'")

        # Validate Generators
        generators = config["generators"]
        for gen_name, gen_config in generators.items():
            if not isinstance(gen_config, dict):
                errors.append(f"Generator '{gen_name}' configuration must be a mapping")
                continue
            
            if "enabled" not in gen_config:
                errors.append(f"Generator '{gen_name}' missing 'enabled' status")

        return errors
