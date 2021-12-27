import os
import subprocess
import unittest


class TestHelloWorldBundle(unittest.TestCase):

    def test_hello_world(self):
        result = self.run_batect('run')

        self.assertIn('\nHello from the JavaScript application!\n', result.stdout)

    def run_batect(self, task):
        command = ['./batect', '-f=test/sample/batect.yml', '--output=quiet', task]

        env = {
            **os.environ,
            'BATECT_QUIET_DOWNLOAD': 'true',
        }

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        if result.returncode != 0:
            raise AssertionError(f'Command failed with exit code {result.returncode} and output: \n{result.stdout}')

        return result


if __name__ == '__main__':
    unittest.main()
