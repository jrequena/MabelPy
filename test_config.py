from core.config.mabel_config import MabelConfig
import json

def test_config():
    config = MabelConfig.from_file("mabel.yaml")
    
    results = {
        "project_name": config.project_name,
        "namespace": config.project_namespace,
        "framework": config.framework,
        "path_domain": str(config.path_domain),
        "entity_enabled": config.get_generator_config("entity").get("enabled"),
        "php_strict": config.get("php.strict_types"),
        "non_existent": config.get("non.existent", "default_value")
    }
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    test_config()
