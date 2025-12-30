from core.cli.generate_command import GenerateCommand
from core.cli.format_command import FormatCommand
from core.cli.watch_command import WatchCommand
from core.cli.init_command import InitCommand
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
        elif command == "watch":
            WatchCommand(config).execute(argv[2:])
        elif command == "init":
            InitCommand(config).execute(argv[2:])
        elif command == "help":
            self.print_help()
        else:
            print(f"Unknown command: {command}")
            self.print_help()

    def print_help(self):
        print("\033[1;34mMabel PHP Generator CLI\033[0m")
        print("Usage: python3 mabel.py <command> [args]")
        print("\nCommands:")
        print("  \033[1;32minit\033[0m               Interactive wizard to create a new contract")
        print("  \033[1;32mgenerate\033[0m <path>    Generate code from contract (.yaml)")
        print("  \033[1;32mwatch\033[0m [dir]        Watch for changes and re-generate automatically")
        print("  \033[1;32mformat\033[0m              Run PHP-CS-Fixer on generated code")
        print("  \033[1;32mhelp\033[0m                Show this help")
