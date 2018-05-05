import unittest
import fibonacci as f

class Test_Fibonacci(unittest.TestCase):
    def test_accuracy(self):
        n = [0, 1, 10, 45]
        Fn = [0, 1, 55, 1134903170]
        for i in range(0, len(n)):
            assert f.fibonacci(n[i]) == Fn[i]


if __name__ == '__main__':
    unittest.main()
