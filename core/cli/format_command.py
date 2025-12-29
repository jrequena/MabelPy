import subprocess
from pathlib import Path
from core.config import MabelConfig

class FormatCommand:
    def __init__(self, config: MabelConfig):
        self.config = config

    def execute(self, args: list):
        print("Running PHP-CS-Fixer...")
        
        # We assume vendor/bin/php-cs-fixer exists if composer install was run
        # In this environment it won't work, but the code will be ready.
        
        paths = [
            self.config.get("paths.source_root", "src"),
            self.config.get("paths.tests", "tests")
        ]
        
        try:
            cmd = ["vendor/bin/php-cs-fixer", "fix", "--allow-risky=yes"] + paths
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print("✓ Formatting complete")
            else:
                print("✗ Formatting failed or no changes needed")
                print(result.stdout)
                print(result.stderr)
        except FileNotFoundError:
            print("✗ PHP-CS-Fixer not found in vendor/bin/. Please run composer install.")
