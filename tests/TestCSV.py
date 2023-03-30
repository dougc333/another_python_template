#rc = ReadCSV('../data')
#rc = ReadCSV('../data/foo.csv')
#rc = ReadCSV('../tests/no_read_premission.txt')
from unittest import TestCase

class TestExceptions:
    def test_directory_not_file(self):
        self.assertRaises(IsADirectoryError, ReadCSV('../data'))
    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError,ReadCSV('../data/foo.csv'))