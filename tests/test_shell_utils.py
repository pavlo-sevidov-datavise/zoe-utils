import unittest

from utilities.shell_utils import ShellTask


class TestRunCommand(unittest.TestCase):
    def test_run_command_success(self):
        self.assertIn("success", ShellTask("echo success").run())

    def test_run_command_fail(self):
        self.assertIn("error", ShellTask("false").run())


if __name__ == '__main__':
    unittest.main()
