class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        l = []
        for i in brokenLetters:
            l.append(i)
        count = 0
        t = text.split()
        for i in t:
            valid = True
            for j in i:
                if j in l:
                    valid = False
                    break
            if (valid):
                count += 1

        return count