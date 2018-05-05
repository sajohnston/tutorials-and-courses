import unittest
import least_common_multiple as l

class Test_LeastCommonMultiple(unittest.TestCase):
    def test_basic_accuracy(self):
        a = [6, 28851538]
        b = [8, 1183019]
        out = [24, 1933053046]
        for i in range(0, len(a)):
            assert l.lcm(a[i], b[i]) == out[i]

    def test_duplicate_input(self):
        abOut = [1, 2, 3, 4, 5]
        for i in range(0, len(abOut)):
            assert l.lcm(abOut[i], abOut[i]) == abOut[i]

    def test_switch_input(self):
        a = [5, 3]
        b = [3, 5]
        out = 15
        for i in range(0, len(a)):
            assert l.lcm(a[i], b[i]) == out

    def test_divisor_self(self):
        a = [1, 2, 3, 4, 10000000]
        bOut = [2, 8, 9, 24, 500000000]
        for i in range(0, len(a)):
            assert l.lcm(a[i], bOut[i]) == bOut[i]
        
if __name__ == '__main__':
    unittest.main()
