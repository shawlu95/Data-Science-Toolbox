class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool

        When reading from the i-th position,
        if bits[i] == 0, the next character must
        have 1 bit; else if bits[i] == 1, the next
        character must have 2 bits. We increment
        our read-pointer i to the start of the next
        character appropriately. At the end, if our
        pointer is at bits.length - 1, then the last
        character must have a size of 1 bit.
        """
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

    def isOneBitCharacterBit(self, bits):
        # if it pops zero, parity = 0
        parity = bits.pop()
        while bits and bits.pop():
            # flip parity, count
            # parity = 0 if even number of 1
            # parity = 1 if odd number of 1
            parity ^= 1
        return parity == 0

solver = Solution()
print(solver.isOneBitCharacterBit([1, 1, 0, 1, 1, 0]))