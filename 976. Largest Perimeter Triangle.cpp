class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
        // Sort the sides in descending order
        sort(nums.begin(), nums.end(), greater<int>());
        // Check each triplet from largest to smallest
        for (int i = 0; i < nums.size() - 2; ++i) {
            // If the sum of the two smaller sides is greater than the largest, it's a valid triangle
            if (nums[i] < nums[i+1] + nums[i+2]) {
                // Return the perimeter
                return nums[i] + nums[i+1] + nums[i+2];
            }
        }
        // If no valid triangle found, return 0
        return 0;
    }
};