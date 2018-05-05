import unittest
import greatest_common_divisor as g

class Test_GreatestCommonDivisor(unittest.TestCase):
    def test_accuracy(self):
        a = [18, 28851538]
        b = [35, 1183019]
        out = [1, 17657]
        for i in range(0, len(a)):
            print(i)
            assert g.gcd(a[i], b[i]) == out[i]


if __name__ == '__main__':
    unittest.main()
