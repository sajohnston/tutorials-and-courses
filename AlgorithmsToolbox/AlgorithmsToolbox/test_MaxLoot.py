import unittest
import max_loot as ml

class Test_MaxLoot(unittest.TestCase):
    def test_basic(self):
        n = [3, 1]
        W = [50, 10]
        vw = [[[60, 20], [100, 50], [120, 30]], [[500, 30]]]
        out = [180.0000, 166.6667]
        for i in range(len(n)):
            maxLootOut = ml.max_loot(n[i], W[i], vw[i])
            print(i)
            print(maxLootOut)
            assert maxLootOut == out[i]

    def test_max_weight_exceeds_item_weight(self):
        n = [3, 1]
        W = [50, 10]
        vw = [[[60, 1], [100, 1], [120, 1]], [[500, 3]]]
        out = [280.0000, 500.0000]
        for i in range(len(n)):
            assert ml.max_loot(n[i], W[i], vw[i]) == out[i]


if __name__ == '__main__':
    unittest.main()
