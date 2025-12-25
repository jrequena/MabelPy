from core.cli.generate_command import GenerateCommand
from core.config.loader import ConfigLoader

class Kernel:
    def run(self, argv):
        config = ConfigLoader().load()

        command = argv[1] if len(argv) > 1 else None

        if command == "generate":
            GenerateCommand(config).execute(argv[2:])
        else:
            print("Unknown command")
