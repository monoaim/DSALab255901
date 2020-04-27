import unittest
from IPython.display import Markdown, display

import __main__

def printmd(string):
    display(Markdown(string))

class TestPostfixToInfix(unittest.TestCase):
    
    def test_case1(self, queueObj):
        queueObj.enqueue('E')
        queueObj.enqueue('A')
        queueObj.enqueue('S')
        item = queueObj.dequeue()
        self.assertEqual(item, 'E')
        self.assertEqual(queueObj.size(), 2)
        queueObj.enqueue('Y')
        item = queueObj.dequeue()
        self.assertEqual(item, 'A')
        self.assertEqual(queueObj.size(), 2)
        queueObj.enqueue('Q')
        queueObj.enqueue('U')
        queueObj.enqueue('E')
        self.assertEqual(queueObj.size(), 5)
        self.assertEqual(queueObj.dequeue(), 'S')
        self.assertEqual(queueObj.dequeue(), 'Y')
        self.assertEqual(queueObj.dequeue(), 'Q')
        self.assertEqual(queueObj.size(), 2)
        queueObj.enqueue('S')
        queueObj.enqueue('T')
        self.assertEqual(queueObj.size(), 4)
        self.assertEqual(queueObj.dequeue(), 'U')
        self.assertEqual(queueObj.dequeue(), 'E')
        self.assertEqual(queueObj.dequeue(), 'S')
        self.assertEqual(queueObj.size(), 1)
        queueObj.enqueue('I')
        queueObj.enqueue('O')
        self.assertEqual(queueObj.size(), 3)
        self.assertEqual(queueObj.dequeue(), 'T')
        self.assertEqual(queueObj.size(), 2)
        queueObj.enqueue('N')
        self.assertEqual(queueObj.size(), 3)
        self.assertEqual(queueObj.dequeue(), 'I')
        self.assertEqual(queueObj.dequeue(), 'O')
        self.assertEqual(queueObj.dequeue(), 'N')
        self.assertEqual(queueObj.size(), 0)
        # test dequeue from an empty queue
        with self.assertRaises(AssertionError):
            queueObj.dequeue()
            queueObj.dequeue()

    def test_case2(self, hotpotatoSimulator):
        lineup = ["Bill","David","Susan","Jane","Kent","Brad"]
        self.assertEqual(hotpotatoSimulator(7, lineup), "Susan")
        self.assertEqual(hotpotatoSimulator(5, lineup), "Jane")

        lineup = ["Bill","David","Susan","Jane"]
        self.assertEqual(hotpotatoSimulator(2, lineup), "Bill")

        lineup = [str(i) for i in range(1, 42)]
        self.assertEqual(hotpotatoSimulator(3, lineup), "11")


def run_check(func, test_case):
    test = TestPostfixToInfix()
    try:
        getattr(test, test_case)(func)
    except test.failureException as e:
        printmd('**<span style="color: red;">FAILED</span>**')
        print(e)
        return
    printmd('**<span style="color: green;">Tested %s with %s: PASSED</span>**' % (func, test_case))

