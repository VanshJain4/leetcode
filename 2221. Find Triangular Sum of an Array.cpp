class Solution {
public:
    int triangularSum(vector<int>& nums) {
        while (nums.size() > 1) {
            vector<int> newNums;
            newNums.resize(nums.size() - 1);
            for(int i = 0;i < nums.size() -1; i++) {
                newNums[i] = (nums[i] +nums[i+1]) % 10;
            }
            std::copy(newNums.begin(), newNums.end(), std::back_inserter(nums));
            nums = newNums;
        }
        return nums[0];
    }
};