class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j+=1
            group = j - i
            if (group > 1):
                count += group -1
            i = j
        
        return count