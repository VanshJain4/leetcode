class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Helper function to check if a number contains zero
        def has_zero(x):
            return '0' in str(x)
        
        # Try all possible pairs a + b = n, starting from 1
        for a in range(1, n):
            b = n - a
            # Both a and b must not contain zero
            if not has_zero(a) and not has_zero(b):
                return [a, b]

        