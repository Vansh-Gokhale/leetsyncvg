class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        return max(
            (count[num] + count[num + 1] for num in count if num + 1 in count),
            default=0
        )