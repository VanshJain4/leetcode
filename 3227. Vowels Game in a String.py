class Solution:
    def doesAliceWin(self, s: str) -> bool:
        l = []
        turn = True
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                l.append(i)
        
        size = len(l)
        if (size == 0):
            return False
        while size > 0:
            if turn:
                if (size % 2 == 0):
                    size = 1
                else : 
                    size = 0
                turn = False
            else :
                if (size % 2 == 0):
                    size = 0
                else : 
                    size = 1
                turn = True

        return not turn