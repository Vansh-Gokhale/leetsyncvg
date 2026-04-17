class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def build_range(l, r):
            return str(nums[l]) if l == r else f"{nums[l]}->{nums[r]}"

        res = []
        i, n = 0, len(nums)

        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            res.append(build_range(i, j))
            i = j + 1

        return res