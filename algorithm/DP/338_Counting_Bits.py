class Solution:
    # MSB
    def countBits(self, num: int) -> List[int]:
        # [0, b] is calculated
        ans = [0] * (num + 1)
        i, b = 0, 1
        while b <= num:
            # generate [b, 2b) or [b, num) from [0, b)
            while i < b and i + b <= num:
                ans[i + b] = ans[i] + 1
                i += 1
            i = 0
            b *= 2
        return ans

    # LSB: P(x)=P(x/2)+(xmod2)
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(num + 1): # include i == num
            ans[i] = ans[i // 2] + i % 2
        return ans

    # last set bit
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            # reset last bit to 0
            # 01(1) & 00(0) -> 0
            # 10(2) & 01(1) -> 0
            # 11(3) & 10(2) -> 10
            # 1001(9) & 1000(8) -> 1000(8)
            # 1010(10) && 1001(9) -> 1000(8)
            # 1011(11) && 1010(10) -> 1010(10)
            
            # i must start with 1, or i - 1 is negative
            
            ans[i] = ans[i & (i - 1)] + 1
            print(i & (i - 1) )
        return ans