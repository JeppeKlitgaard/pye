import unittest
import pep8
import os
import fnmatch
from os import path
import pye


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        code_path = path.join(path.abspath(pye.__file__), "..", "..")
        code_path = path.abspath(code_path)

        files = []

        for root, dirnames, filenames in os.walk(code_path):
            for filename in fnmatch.filter(filenames, "*.py"):
                files.append(os.path.join(root, filename))

        result = pep8style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings)")

if __name__ == "__main__":
    unittest.main()
