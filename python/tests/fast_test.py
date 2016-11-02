import unittest
import sys
import os.path
sys.path.insert(0, os.path.abspath(".."))  #for import problems be successful
import problems

class fastTest(unittest.TestCase):
    
    def test_p001(self):
        assert_string = "expected answer doesn't match my answer"
        self.assertEqual(problems.p001.p001(), problems.p001.correct_answer, \
                        assert_string)
    
    def test_p002(self):
        assert_string = "expected answer doesn't match my answer"
        self.assertEqual(problems.p002.p002(), problems.p002.correct_answer, \
                        assert_string)

    def test_p003(self):
        assert_string = "expected answer doesn't match my answer"
        self.assertEqual(problems.p003.p003(), problems.p003.correct_answer, \
                         assert_string)

    def test_p004(self):
        assert_string = "expected answer doesn't match my answer"
        self.assertEqual(problems.p004.p004(), problems.p004.correct_answer, \
                         assert_string)
        
    def test_p005(self):
        pass
    '''
        a = problems.p005.correct_answer
        b = problems.p005.p005()
        assert_string = "expected={} doesn't match my answer={}".format(a,b)
        self.assertEqual(problems.p005.p005(), problems.p005.correct_answer, \
                         assert_string)
    '''
    
    def test_p006(self):
        a = problems.p006.correct_answer
        b = problems.p006.p006()
        assert_string = "expected={} doesn't match my answer={}".format(a,b)
        self.assertEqual(a, b, assert_string)



if __name__ == '__main__':
    unittest.main()
