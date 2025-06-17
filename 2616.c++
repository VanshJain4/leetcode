#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool canPair(vector<int> &nums, int p, int maxDiff) {
        int pairs = 0;
        for (int i = 0; i < (int)nums.size() - 1;) {
            if (nums[i+1] - nums[i] <= maxDiff) {
                pairs++;
                i += 2;
                if (pairs >= p) return true;
            } else {
                i++;
            }
        }
        return false;
    }

    int minimizeMax(vector<int> &nums, int p) {
        if (p == 0) return 0;

        sort(nums.begin(), nums.end());

        int left = 0;
        int right = nums.back() - nums.front();

        while (left < right) {
            int mid = left + (right - left)/2;

            if (canPair(nums, p, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
};