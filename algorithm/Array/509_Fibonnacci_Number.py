class Solution:
    def fib(self, N: int) -> int:
        # N is index, not length
        length = N + 1
        buffer = [0] * length
        if N > 0:
            buffer[1] = 1
            for i in range(2, length):
                buffer[i] = buffer[i - 1] + buffer[i - 2]
        return buffer[-1]

    def fib1(self, N: int) -> int:
        a1, a2 = 0, 1
        for _ in range(N):
            a1, a2 = a2, a1 + a2
        return a1

