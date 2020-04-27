import unittest
from IPython.display import Markdown, display

import __main__

def printmd(string):
    display(Markdown(string))

class TestMineSweeper(unittest.TestCase):
    
    def test_case1(self, targetfunc):
        output = targetfunc('t1.in')
        correct_output = ''.join(open('t1.out').readlines())
        self.assertEqual(output, correct_output)

    def test_case2(self, targetfunc):
        output = targetfunc('t2.in')
        correct_output = ''.join(open('t2.out').readlines())
        self.assertEqual(output, correct_output)


def run_check(func, test_case):
    test = TestMineSweeper()
    try:
        getattr(test, test_case)(func)
    except test.failureException as e:
        printmd('**<span style="color: red;">FAILED</span>**')
        print(e)
        return
    printmd('**<span style="color: green;">Tested %s with %s: PASSED</span>**' % (func, test_case))
