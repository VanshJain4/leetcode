class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            new_part = ""
            for c in word:
                if c == 'z':
                    new_part += 'a'  
                else:
                    new_part += chr(ord(c) + 1)
            word += new_part
        return word[k-1]
        