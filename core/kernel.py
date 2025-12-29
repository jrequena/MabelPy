from core.cli.generate_command import GenerateCommand
from core.cli.format_command import FormatCommand
from core.config import MabelConfig

class Kernel:
    def run(self, argv):
        if len(argv) < 2:
            self.print_help()
            return

        config = MabelConfig.from_file()
        command = argv[1]

        if command == "generate":
            GenerateCommand(config).execute(argv[2:])
        elif command == "format":
            FormatCommand(config).execute(argv[2:])
        elif command == "help":
            self.print_help()
        else:
            print(f"Unknown command: {command}")
            self.print_help()

    def print_help(self):
        print("Mabel PHP Generator CLI")
        print("Usage: python3 mabel.py <command> [args]")
        print("\nCommands:")
        print("  generate <contract>  Generate code from contract")
        print("  format               Run PHP-CS-Fixer on generated code")
        print("  help                 Show this help")
