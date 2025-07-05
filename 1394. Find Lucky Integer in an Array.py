from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luck = -1
        freq = Counter(arr)
        for num in freq:
            if num == freq[num]:
                luck = max(luck, num)
        return luck
