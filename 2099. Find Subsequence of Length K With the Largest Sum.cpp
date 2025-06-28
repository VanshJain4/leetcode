class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        int n = nums.size();
        vector<bool> used(n, false);
        for (int t = 0; t < k; ++t) {
            int maxVal = INT_MIN;
            int maxIdx = -1;
            for (int i = 0; i < n; ++i) {
                if (!used[i] && nums[i] > maxVal) {
                    maxVal = nums[i];
                    maxIdx = i;
                }
            }
            used[maxIdx] = true;
        }

        // Step 2: Build the result vector in original order
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (used[i]) result.push_back(nums[i]);
        }

        return result;
    }
};
