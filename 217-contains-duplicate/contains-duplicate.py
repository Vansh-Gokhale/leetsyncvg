from typing import List
from itertools import pairwise

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        return any(a == b for a, b in pairwise(sorted_nums))