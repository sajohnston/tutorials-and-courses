import unittest
import fibonacci_last_digit as f

class Test_FibonacciLastDigit(unittest.TestCase):
    def test_accuracy(self):
        n = [0, 1, 10, 200, 331, 327305]
        FnLastDigit = [0, 1, 5, 5, 9, 5]
        for i in range(0,len(n)):
            assert f.get_fibonacci_last_digit(n[i]) == FnLastDigit[i] 

if __name__ == '__main__':
    unittest.main()
