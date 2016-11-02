import unittest
import sys
import os.path
sys.path.insert(0, os.path.abspath(".."))  #for import problems be successful
import problems

class firstSimpleTest(unittest.TestCase):
    
    def test_p001(self):
        problems.p001.fast_main()


if __name__ == '__main__':
    unittest.main()
