class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {}
        consonants = {}

        for i in s:
            if i in "aeiou":
                vowel[i] = vowel.get(i, 0) + 1
            else:
                consonants[i] = consonants.get(i, 0) + 1

        max_v = max(vowel.values()) if vowel else 0
        max_c = max(consonants.values()) if consonants else 0

        return max_v + max_c
