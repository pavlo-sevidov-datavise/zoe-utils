import unittest
from subprocess import CalledProcessError

from utilities.shell_utils import ShellTask


class TestRunCommand(unittest.TestCase):
    def test_run_command_success(self):
        successful_return_code = 0
        self.assertEqual(successful_return_code, ShellTask("echo success").run())

    def test_run_command_fail(self):
        with self.assertRaises(expected_exception=CalledProcessError):
            ShellTask("false").run()


if __name__ == '__main__':
    unittest.main()
