import yaml
from pathlib import Path

class InitCommand:
    def __init__(self, config):
        self.config = config

    def execute(self, args: list):
        print("🚀 Mabel Interactive Contract Generator")
        print("This will help you create a basic contract YAML.\n")

        module_name = input("Module Name (e.g. Order): ").strip()
        if not module_name:
            print("Module name is required.")
            return

        namespace = input(f"Namespace [App\\Module\\{module_name}]: ").strip() or f"App\\Module\\{module_name}"
        entity_name = input(f"Primary Entity Name [{module_name}]: ").strip() or module_name
        
        table_name = input(f"Database Table [{entity_name.lower()}s]: ").strip() or f"{entity_name.lower()}s"

        contract = {
            "module": {
                "name": module_name,
                "namespace": namespace,
                "framework": "laravel"
            },
            "database": {
                "driver": "mysql",
                "orm": "eloquent",
                "table": table_name
            },
            "entities": {
                entity_name: {
                    "id": "int",
                    "created_at": "datetime"
                }
            },
            "use_cases": {
                f"Create{entity_name}": {
                    "description": f"Create a new {entity_name}",
                    "input": {
                        "name": "string"
                    },
                    "output": entity_name,
                    "rules": [
                        {"set_default": "created_at = now()"}
                    ]
                }
            },
            "metadata": {
                "version": "0.1.0"
            }
        }

        output_path = Path(f"contracts/{entity_name}.yaml")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w') as f:
            yaml.dump(contract, f, sort_keys=False)

        print(f"\n✅ Contract created successfully at {output_path}")
        print(f"You can now run: python3 mabel.py generate {output_path}")
