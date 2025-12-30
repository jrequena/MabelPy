Run pytest tests/python
============================= test session starts ==============================
platform linux -- Python 3.12.12, pytest-7.4.3, pluggy-1.6.0
rootdir: /home/runner/work/MabelPy/MabelPy
plugins: snapshot-0.9.0
collected 9 items

tests/python/test_generators.py FF                                       [ 22%]
tests/python/test_validator.py .......                                   [100%]

=================================== FAILURES ===================================
_________________________ test_dto_generation_snapshot _________________________

config = <core.config.mabel_config.MabelConfig object at 0x7f63ad0c6900>
snapshot = <pytest_snapshot.plugin.Snapshot object at 0x7f63ad1a4e60>
tmp_path = PosixPath('/tmp/pytest-of-runner/pytest-0/test_dto_generation_snapshot0')

    def test_dto_generation_snapshot(config, snapshot, tmp_path):
        generator = PhpDtoGenerator(config)
        contract = {
            "entity": {"name": "User"},
            "fields": [
                {"name": "id", "type": "int"},
                {"name": "name", "type": "string"},
                {"name": "status", "type": "UserStatus"}
            ],
            "enums": {"UserStatus": {"type": "string", "values": ["ACTIVE"]}}
        }
    
        # Generate to tmp_path
        generator.generate(contract, tmp_path)
    
        # Check generated file
        domain_suffix = config.get_generator_config("entity").get("namespace_suffix", "Domain")
        generated_file = tmp_path / domain_suffix / "User.php"
    
        assert generated_file.exists()
>       snapshot.assert_match(generated_file.read_text(), "UserDTO.php")
E       AssertionError: value does not match the expected value in snapshot tests/python/snapshots/test_generators/test_dto_generation_snapshot/UserDTO.php
E         (run pytest with --snapshot-update to update snapshots)
E       assert '<?php\n\ndec...{\n    }\n}\n' == '<?php\n\ndec...) {\n    }\n}'
E         Skipping 260 identical leading characters in diff, use -v to show
E           ) {
E               }
E         - }
E         + }

tests/python/test_generators.py:30: AssertionError
________________________ test_enum_generation_snapshot _________________________

config = <core.config.mabel_config.MabelConfig object at 0x7f63add75eb0>
snapshot = <pytest_snapshot.plugin.Snapshot object at 0x7f63ad198260>
tmp_path = PosixPath('/tmp/pytest-of-runner/pytest-0/test_enum_generation_snapshot0')

    def test_enum_generation_snapshot(config, snapshot, tmp_path):
        generator = PhpEnumGenerator(config)
        enum_name = "UserStatus"
        enum_def = {
            "type": "string",
            "values": ["ACTIVE", "INACTIVE", "PENDING"]
        }
    
        generator.generate(enum_name, enum_def, tmp_path)
    
        domain_suffix = config.get_generator_config("entity").get("namespace_suffix", "Domain")
        generated_file = tmp_path / domain_suffix / "Enum" / "UserStatus.php"
    
        assert generated_file.exists()
>       snapshot.assert_match(generated_file.read_text(), "UserStatusEnum.php")
E       AssertionError: value does not match the expected value in snapshot tests/python/snapshots/test_generators/test_enum_generation_snapshot/UserStatusEnum.php
E         (run pytest with --snapshot-update to update snapshots)
E       assert "<?php\n\ndec...ENDING';\n}\n" == "<?php\n\ndec...'PENDING';\n}"
E         Skipping 167 identical leading characters in diff, use -v to show
E           PENDING';
E         - }
E         + }

tests/python/test_generators.py:46: AssertionError
=========================== short test summary info ============================
FAILED tests/python/test_generators.py::test_dto_generation_snapshot - AssertionError: value does not match the expected value in snapshot tests/python/snapshots/test_generators/test_dto_generation_snapshot/UserDTO.php
  (run pytest with --snapshot-update to update snapshots)
assert '<?php\n\ndec...{\n    }\n}\n' == '<?php\n\ndec...) {\n    }\n}'
  Skipping 260 identical leading characters in diff, use -v to show
    ) {
        }
  - }
  + }
FAILED tests/python/test_generators.py::test_enum_generation_snapshot - AssertionError: value does not match the expected value in snapshot tests/python/snapshots/test_generators/test_enum_generation_snapshot/UserStatusEnum.php
  (run pytest with --snapshot-update to update snapshots)
assert "<?php\n\ndec...ENDING';\n}\n" == "<?php\n\ndec...'PENDING';\n}"
  Skipping 167 identical leading characters in diff, use -v to show
    PENDING';
  - }
  + }
========================= 2 failed, 7 passed in 0.10s ==========================
Error: Process completed with exit code 1.