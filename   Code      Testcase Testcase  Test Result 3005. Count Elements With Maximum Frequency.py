from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count frequency of each element
        freq = Counter(nums)
        # Find the maximum frequency
        max_freq = max(freq.values())
        # Sum frequencies of all elements with max frequency
        return sum(count for count in freq.values() if count == max_freq)