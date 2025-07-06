class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        count = 1
        i = 1
        nums.sort()
        start = nums[0]
        if (len(nums) == 1):
            return 1
        while i < len(nums):
            if nums [i] - start <= k:
                i = i + 1
            else:
                count = count + 1
                start = nums[i]
                i=i+1

        return count
