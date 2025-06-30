class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxl = 0
        for n in freq:
            if n + 1 in freq:
                maxl = max(maxl, freq[n] + freq[n + 1])
        return maxl
        