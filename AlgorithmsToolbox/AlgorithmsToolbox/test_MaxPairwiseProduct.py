import unittest
import max_pairwise_prod_fast as m

class Test_MaxPairwiseProduct(unittest.TestCase):
    def testBasicInput(self):
        n = 5
        A = [1, 2, 3, 4, 5]
        assert m.max_pairwise_product_fast(n, A) == 20

        n = 2
        A = [1, 2]
        assert m.max_pairwise_product_fast(n, A) == 2

        n = 4
        A = [4, 3, 2, 1]
        assert m.max_pairwise_product_fast(n, A) == 12

        n = 3
        A = [100, 200, 50]
        assert m.max_pairwise_product_fast(n, A) == 20000


    def testReverseSequence(self):
        n = 2
        A1 = [1, 2]
        A2 = [2, 1]
        assert m.max_pairwise_product_fast(n, A1) == m.max_pairwise_product_fast(n, A2)
 

    def testLargerInput(self):
        n = 2
        A = [100000, 90000]
        assert m.max_pairwise_product_fast(n, A) == 9000000000
 

    def testNonUniqueInput(self):
        n = 3
        A = [1, 4, 4]
        assert m.max_pairwise_product_fast(n, A) == 16

        n = 2
        A = [1, 1]
        assert m.max_pairwise_product_fast(n, A) == 1



if __name__ == '__main__':
    unittest.main()
