class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK, MAX = 0xFFFFFFFF, 0x7FFFFFFF
        a, b = a & MASK, b & MASK
        while b:
            a, b = (a ^ b), ((a & b) << 1) & MASK
        return a if a <= MAX else ~(a ^ MASK)