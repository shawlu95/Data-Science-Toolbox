# python3 -m unittest fibonacci_test.py
import unittest
from fibonacci import F, sum_fib, sum_fib_dp

class TestFibonacciSum(unittest.TestCase):
    def test_F(self):
        self.assertEqual(F(0), 0)
        self.assertEqual(F(4), 3)
        self.assertEqual(F(5), 5)
        self.assertEqual(F(6), 8)
        self.assertEqual(F(7), 13)

    def test_sum_fib(self):
        self.assertEqual(sum_fib(1, 1), 1)
        self.assertEqual(sum_fib(1, 2), 2)
        self.assertEqual(sum_fib(1, 3), 4)
        self.assertEqual(sum_fib(1, 5), 12)

    def test_sum_fib_dp(self):
        self.assertEqual(sum_fib(1, 1), sum_fib_dp(1, 1))
        self.assertEqual(sum_fib(1, 2), sum_fib_dp(1, 2))
        self.assertEqual(sum_fib(1, 3), sum_fib_dp(1, 3))
        self.assertEqual(sum_fib(1, 5), sum_fib_dp(1, 5))

        # large m, n
        for n in range(1000, 1100):
            m = n + 10
            self.assertEqual(sum_fib(n, m), sum_fib_dp(n, m))

        # m, n
        for n in range(1000, 1100):
            self.assertEqual(sum_fib(n, n), sum_fib_dp(n, n))
