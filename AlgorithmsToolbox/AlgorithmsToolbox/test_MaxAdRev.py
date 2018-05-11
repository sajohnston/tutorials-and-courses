import unittest
import max_ad_revenue as m

class Test_MaxAdRev(unittest.TestCase):
    def test_basic_accuracy(self):
        assert m.max_ad_revenue([23], [39]) == 897
        assert m.max_ad_revenue([1, 3, -5], [-2, 4, 1]) == 23

if __name__ == '__main__':
    unittest.main()
