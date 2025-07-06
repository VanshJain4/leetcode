class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0  # binary value built so far
        length = 0  # length of the subsequence
        power = 0   # 2^0, 2^1, ...

        # Go from right to left (least significant to most)
        for ch in reversed(s):
            if ch == '0':
                # Always safe to add a 0
                length += 1
            else:
                # Try to add a '1' if it keeps value ≤ k
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    length += 1
            power += 1
        
        return length
