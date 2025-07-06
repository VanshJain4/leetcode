class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        min_deletions = float('inf')
        for i in range(len(freq)):
            target = freq[i]
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f  
                elif f > target + k:
                    deletions += f - (target + k) 
            min_deletions = min(min_deletions, deletions)

        return min_deletions

            
        