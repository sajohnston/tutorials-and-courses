import unittest
import moneychange as mc

class Test_MoneyChange(unittest.TestCase):
    def test_basic_accuracy(self):
        m = [2, 28]
        out = [2, 6]
        for i in range(0, len(m)):
            assert mc.change_money(m[i]) == out[i]

if __name__ == '__main__':
    unittest.main()
