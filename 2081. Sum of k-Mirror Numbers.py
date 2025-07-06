class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        count = 0
        length = 1

        # Continue until we find n k-mirror numbers
        while count < n:
            # Generate palindromes with odd length
            start = 10 ** (length - 1)
            end = 10 ** length
            for i in range(start, end):
                if count >= n:
                    break
                p = self.createPalindrome(i, odd=True)
                if self.isPalindrome(p, k):
                    total += p
                    count += 1

            # Generate palindromes with even length
            for i in range(start, end):
                if count >= n:
                    break
                p = self.createPalindrome(i, odd=False)
                if self.isPalindrome(p, k):
                    total += p
                    count += 1

            length += 1

        return total
