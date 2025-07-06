class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1,n):
            pow2[i] = (pow2[i-1] * 2) % mod
        res = 0
        left = 0
        right = n - 1


        while left <= right:
            if nums[left] + nums[right ] <= target:
                res += pow2[right - left]
                res %= mod
                left += 1
            else:
                right -= 1

        return res