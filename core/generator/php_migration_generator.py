from pathlib import Path
from datetime import datetime
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpMigrationGenerator(BaseGenerator):
    TYPE_MAP = {
        "int": "integer",
        "string": "string",
        "bool": "boolean",
        "float": "float",
        "datetime": "timestamp",
        "Id": "bigInteger",
        "Uuid": "uuid"
    }

    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        # We generate migrations based on database config if present
        db_config = contract.get("database", {})
        if not db_config:
            return []

        generated_files = []
        entities = contract.get("entities", {})
        
        # We'll use a timestamp for the migration filename to follow Laravel convention
        timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        
        for entity_name, fields in entities.items():
            # For simplicity, table name is plural of entity or from entity meta
            table_name = entity_name.lower() + "s" 
            if entity_name == "User": table_name = "users" # match contract example
            
            migration_fields = self._prepare_migration_fields(fields)
            
            context = {
                "table_name": table_name,
                "fields": migration_fields
            }
            
            template = self.load_template("migration.php.tpl")
            content = self.render(template, context)
            
            migration_dir = output_dir.parent / "database" / "migrations"
            migration_dir.mkdir(parents=True, exist_ok=True)
            
            file_name = f"{timestamp}_create_{table_name}_table.php"
            file_path = migration_dir / file_name
            file_path.write_text(content)
            generated_files.append(file_path)
            
        return generated_files

    def _prepare_migration_fields(self, fields: dict) -> list:
        lines = []
        for name, f_def in fields.items():
            if name == "id":
                lines.append({"line": "$table->id()"})
                continue
                
            # Handle Relationships for Foreign Keys
            if isinstance(f_def, dict):
                if "belongs_to" in f_def:
                    target = f_def["belongs_to"].lower()
                    lines.append({"line": f"$table->foreignId('{target}_id')->constrained()"})
                    continue
                if "has_many" in f_def or "has_one" in f_def:
                    # These don't usually add a column to THIS table (except maybe has_one if one-sided)
                    continue

                raw_type = f_def.get("type", "string")
                nullable = f_def.get("nullable", False)
            else:
                raw_type = f_def
                nullable = False

            laravel_type = self.TYPE_MAP.get(raw_type, "string")
            line = f"$table->{laravel_type}('{name}')"
            if nullable:
                line += "->nullable()"
            
            lines.append({"line": line})
            
        return lines
