class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            if l < len(nums) and nums[l] == target:
                ans = l
            return ans

        def find_last():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            if r >= 0 and nums[r] == target:
                return r
            return -1

        return [find_first(), find_last()]