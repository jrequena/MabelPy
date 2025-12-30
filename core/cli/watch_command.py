import time
from pathlib import Path
from core.cli.generate_command import GenerateCommand

class WatchCommand:
    def __init__(self, config):
        self.config = config
        self.generator = GenerateCommand(config)

    def execute(self, args: list):
        path_to_watch = Path(args[0]) if args else Path("contracts")
        
        if not path_to_watch.exists():
            print(f"Error: Path {path_to_watch} does not exist")
            return

        print(f"👀 Watching for changes in {path_to_watch}...")
        print("Press Ctrl+C to stop")

        last_mtimes = self._get_mtimes(path_to_watch)

        try:
            while True:
                time.sleep(1)
                current_mtimes = self._get_mtimes(path_to_watch)
                
                changed_files = []
                for file_path, mtime in current_mtimes.items():
                    if file_path not in last_mtimes or mtime > last_mtimes[file_path]:
                        changed_files.append(file_path)

                if changed_files:
                    for file_path in changed_files:
                        if file_path.suffix in ['.yaml', '.yml']:
                            print(f"\n✨ Change detected in {file_path.name}, re-generating...")
                            self.generator.execute([str(file_path)])
                    
                    last_mtimes = current_mtimes
        except KeyboardInterrupt:
            print("\nStopped watching.")

    def _get_mtimes(self, path: Path):
        mtimes = {}
        if path.is_file():
            mtimes[path] = path.stat().st_mtime
        else:
            for file in path.glob("*.y*ml"):
                mtimes[file] = file.stat().st_mtime
        return mtimes
