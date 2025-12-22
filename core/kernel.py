from core.cli.generate_command import GenerateCommand

class Kernel:
    def run(self, argv):
        if len(argv) < 2:
            print("Available commands:")
            print("  generate <contract.yaml>")
            return

        command = argv[1]

        if command == "generate":
            GenerateCommand().execute(argv[2:])
        else:
            print(f"Unknown command: {command}")
