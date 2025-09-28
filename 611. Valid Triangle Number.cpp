class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        // Sort the array to make triangle checks easier
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int count = 0;
        
        // Fix the largest side at index k, and find pairs (i, j) such that nums[i] + nums[j] > nums[k]
        for (int k = n - 1; k >= 2; --k) {
            int i = 0, j = k - 1;
            while (i < j) {
                // If nums[i] + nums[j] > nums[k], all pairs (i, i+1, ..., j-1) with j are valid
                if (nums[i] + nums[j] > nums[k]) {
                    count += (j - i); // All these pairs work
                    --j; // Try a smaller j
                } else {
                    ++i; // Try a bigger i
                }
            }
        }
        return count;
    }
};