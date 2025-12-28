from core.cli.generate_command import GenerateCommand
from core.config import MabelConfig

class Kernel:
    def run(self, argv):
        config = MabelConfig.from_file()

        command = argv[1] if len(argv) > 1 else None

        if command == "generate":
            GenerateCommand(config).execute(argv[2:])
        else:
            print("Unknown command")
