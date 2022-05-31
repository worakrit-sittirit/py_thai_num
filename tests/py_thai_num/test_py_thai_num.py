import unittest
import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', '..', 'src', 'py_thai_num' )
sys.path.append( mymodule_dir )
from py_thai_num import py_thai_num
from py_thai_num import file_thai_num


class TestThaiNumCon(unittest.TestCase):

    def test_char(self):
        self.assertEqual(py_thai_num.to_char("๑"), "1")
        self.assertEqual(py_thai_num.to_char("๒"), "2")
        self.assertEqual(py_thai_num.to_char("๓"), "3")
        self.assertEqual(py_thai_num.to_char("๔"), "4")
        self.assertEqual(py_thai_num.to_char("๕"), "5")
        self.assertEqual(py_thai_num.to_char("๖"), "6")
        self.assertEqual(py_thai_num.to_char("๗"), "7")
        self.assertEqual(py_thai_num.to_char("๘"), "8")
        self.assertEqual(py_thai_num.to_char("๙"), "9")
        self.assertEqual(py_thai_num.to_char("๐"), "0")

    def test_string(self):
        self.assertEqual(py_thai_num.to_str("๑๒๓๔๕๖๗๘๙๐"), "1234567890")
        self.assertEqual(py_thai_num.to_str("กขคง๑๒๓๔๕๖๗๘๙๐"), "กขคง1234567890")
        self.assertEqual(py_thai_num.to_str("abcd๑๒๓๔๕๖๗๘๙๐"), "abcd1234567890")
        self.assertEqual(py_thai_num.to_str("๑a๒b๓c๔d๕๖๗๘๙๐"), "1a2b3c4d567890")

    def test_integer(self):
        self.assertEqual(py_thai_num.to_int("๑๒๓๔"), 1234)
        self.assertEqual(py_thai_num.to_int("๗๘๙๐"), 7890)

    def test_file_string(self):
        self.assertEqual(file_thai_num.to_str("testcase1"), "กขคง1234567890")
        self.assertEqual(file_thai_num.to_str("testcase2"), "1a2b3c4d567890")

    def test_file_file(self):
        self.assertEqual(file_thai_num.to_file("testcase1","result1"), 0)
        tmp_f = open("result1", "r")
        self.assertEqual(tmp_f.read(), "กขคง1234567890")
        tmp_f.close()


if __name__ == '__main__':
    unittest.main()
