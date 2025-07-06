class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        l_odd =[]
        l_even =[]

        for count in freq.values():
            if (count % 2 == 1):
                l_odd.append(count)
            if (count % 2 == 0):
                l_even.append(count)
        if not l_odd or not l_even:
            return -1

        max_diff = float('-inf')
        for o in l_odd:
            for e in l_even:
                max_diff = max(max_diff, o - e)

        return max_diff
