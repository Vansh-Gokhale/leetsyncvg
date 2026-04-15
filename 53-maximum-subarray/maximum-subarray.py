class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr = nums[0]
        for n in nums[1:]:
            curr = max(curr, 0) + n
            max_sum = max(max_sum, curr)
        return max_sum