class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l =[]
        for i in range(len(nums)):
            if (nums[i] == key):
                l.append(i)
        
        ans = []        
        for i in range(len(l)):
            for j in range(len(nums)):
                if j in ans:
                    continue
                if(abs(j - l[i]) <= k):
                    ans.append(j)

        return ans
