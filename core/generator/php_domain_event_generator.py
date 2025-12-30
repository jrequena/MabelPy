from pathlib import Path
from core.generator.base_generator import BaseGenerator
from core.config import MabelConfig

class PhpDomainEventGenerator(BaseGenerator):
    def __init__(self, config: MabelConfig):
        super().__init__("core/templates/php")
        self.config = config

    def generate(self, contract: dict, output_dir: Path):
        use_cases = contract.get("use_cases", {})
        if not use_cases:
            return []

        entities = list(contract.get("entities", {}).keys())
        primary_entity = entities[0] if entities else None
        
        generated_files = []
        events_to_generate = []

        # Collect all events from emit rules
        for uc_name, uc_def in use_cases.items():
            rules = uc_def.get("rules", [])
            entity_name = uc_def.get("entity", primary_entity)
            
            for rule in rules:
                if "emit" in rule:
                    event_name = rule["emit"]
                    events_to_generate.append({
                        "name": event_name,
                        "entity": entity_name
                    })

        # Generate each unique event
        seen_events = set()
        for event in events_to_generate:
            if event["name"] not in seen_events:
                generated_files.append(self._generate_event(event, output_dir))
                seen_events.add(event["name"])
            
        return generated_files

    def _generate_event(self, event: dict, output_dir: Path):
        base_ns = self.config.project_namespace
        event_name = event["name"]
        entity_name = event["entity"]
        
        # Events go in Domain/Event/{Entity}
        event_suffix = f"Domain/Event/{entity_name}" if entity_name else "Domain/Event"
        target_ns = f"{base_ns}\\{event_suffix.replace('/', '\\')}"
        target_dir = output_dir / event_suffix
        target_dir.mkdir(parents=True, exist_ok=True)

        entity_class = None
        if entity_name:
             # Assume Entity is in Domain namespace
             entity_config = self.config.get_generator_config("entity")
             entity_suffix = entity_config.get("namespace_suffix", "Domain")
             entity_class = f"\\{base_ns}\\{entity_suffix.replace('/', '\\')}\\{entity_name}"

        template = self.load_template("event.php.tpl")
        context = {
            "namespace": target_ns,
            "class_name": event_name,
            "entity_class": entity_class
        }
        
        content = self.render(template, context)
        file_path = target_dir / f"{event_name}.php"
        file_path.write_text(content)
        return file_path
