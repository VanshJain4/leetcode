class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int, long long> cnt;   // use explicit types
        for (int x : power) {
            cnt[x]++;
        }

        vector<pair<int, long long>> a;
        for (auto& [val, count] : cnt) {
            a.push_back({val, val * count});
        }
        sort(a.begin(), a.end());

        int size = a.size();
        vector<long long> dp(size);
        dp[0] = a[0].second;

        for (int i = 1; i < size; i++) {
            int j = i - 1;
            while (j >= 0 && a[i].first - a[j].first <= 2) j--;

            if (j >= 0)
                dp[i] = max(dp[i - 1], a[i].second + dp[j]);
            else
                dp[i] = max(dp[i - 1], a[i].second);
        }

        return dp.back();
    }
};
