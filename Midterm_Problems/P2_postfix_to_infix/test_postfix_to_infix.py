import unittest
from IPython.display import Markdown, display

import __main__

def printmd(string):
    display(Markdown(string))

class TestPostfixToInfix(unittest.TestCase):
    
    def test_case1(self, stackObj):
        # test clear
        stackObj.push(0)
        stackObj.push(2)
        stackObj.push(3)
        stackObj.clear()
        self.assertEqual(True, stackObj.isEmpty())

        # test push, pop
        stackObj.push('P')
        stackObj.push('U')
        stackObj.push('S')
        self.assertEqual('S', stackObj.pop())
        stackObj.push('C')
        self.assertEqual('C', stackObj.pop())
        self.assertEqual('U', stackObj.pop())
        self.assertEqual('P', stackObj.pop())

        # test popping from an empty stack
        with self.assertRaises(AssertionError):
            stackObj.pop()         
            stackObj.pop()         

        # test push, pop
        result = ''
        stackObj.push('E')
        stackObj.push('A')
        stackObj.push('S')
        result += stackObj.pop()
        stackObj.push('Y')
        result += stackObj.pop()
        stackObj.push('Q')
        stackObj.push('U')
        stackObj.push('E')
        result += stackObj.pop()
        result += stackObj.pop()
        result += stackObj.pop()
        stackObj.push('S')
        stackObj.push('T')
        result += stackObj.pop()
        result += stackObj.pop()
        result += stackObj.pop()
        stackObj.push('I')
        stackObj.push('O')
        result += stackObj.pop()
        stackObj.push('N')
        result += stackObj.pop()
        result += stackObj.pop()
        result += stackObj.pop()
        self.assertEqual(result, "SYEUQTSAONIE")

    def test_case2(self, postfixEvaluator):
        with open('t1.in') as ip:
            with open('t1.out') as op:
                while True:
                    postfix = ip.readline().strip()
                    if postfix == '': 
                        break
                    infix, value = op.readline().strip().split()
                    printmd('*<span style="color: black;">%s</span>*' % postfix)
                    self.assertEqual(postfixEvaluator.eval(postfix), int(value))
                    self.assertEqual(postfixEvaluator.postfix_to_infix(postfix), infix)
                    printmd(' ........ ok')

        with open('t2.in') as ip:
            with open('t2.out') as op:
                while True:
                    postfix = ip.readline().strip()
                    if postfix == '': 
                        break
                    infix, value = op.readline().strip().split()
                    printmd('*<span style="color: black;">%s</span>*' % postfix)
                    self.assertEqual(postfixEvaluator.eval(postfix), int(value))
                    self.assertEqual(postfixEvaluator.postfix_to_infix(postfix), infix)
                    printmd(' ........ ok')


def run_check(func, test_case):
    test = TestPostfixToInfix()
    try:
        getattr(test, test_case)(func)
    except test.failureException as e:
        printmd('**<span style="color: red;">FAILED</span>**')
        print(e)
        return
    printmd('**<span style="color: green;">Tested %s with %s: PASSED</span>**' % (func, test_case))

