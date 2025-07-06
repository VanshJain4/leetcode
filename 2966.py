from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        n = len(nums)
        
        while i < n:
            if i + 2 >= n:
                return []  # Not enough elements to form a triplet
            
            group = [nums[i], nums[i+1], nums[i+2]]
            if group[2] - group[0] <= k:
                res.append(group)
                i += 3
            else:
                return []  # Can't form a valid group
        
        return res
