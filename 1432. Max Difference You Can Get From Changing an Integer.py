class Solution:
    def maxDiff(self, num: int) -> int:
        # Step 1: Break number into digits
        l = []
        temp = num
        for _ in range(len(str(num))):
            l.append(temp % 10)
            temp = temp // 10
        l.reverse()

        # Make a copy for minimization
        l2 = l.copy()

        # Step 2: Maximize by replacing first non-9 digit with 9
        max_num = 0
        min_num = 0

        # Find digit to replace for max
        n = -1
        for i in range(len(l)):
            if l[i] != 9:
                n = l[i]
                break

        # Replace all n with 9
        if n != -1:
            for i in range(len(l)):
                if l[i] == n:
                    l[i] = 9

        # Step 3: Minimize by replacing one digit
        # Strategy: Replace first digit ≠ 1 with 1 if at index 0, else 0
        n = -1
        replace_with = 0
        for i in range(len(l2)):
            if l2[i] != 1 and l2[i] != 0:
                n = l2[i]
                replace_with = 1 if i == 0 else 0
                break

        # Replace all n with replace_with
        if n != -1:
            for i in range(len(l2)):
                if l2[i] == n:
                    l2[i] = replace_with

        # Step 4: Convert digit lists back to integers
        for d in l:
            max_num = max_num * 10 + d
        for d in l2:
            min_num = min_num * 10 + d

        return max_num - min_num
