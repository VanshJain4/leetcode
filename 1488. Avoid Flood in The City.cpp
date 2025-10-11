class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
    unordered_map<int, int> full; // Maps lake number to last day it was filled
    set<int> dryDays; // Stores indices of days we can dry a lake
    vector<int> ans(rains.size(), 1); // Default: dry any lake (for dry days)

    for (int i = 0; i < rains.size(); ++i) {
        if (rains[i] > 0) {
            int lake = rains[i];
            if (full.count(lake)) {
                // Find a dry day after last time this lake was filled
                auto it = dryDays.upper_bound(full[lake]);
                if (it == dryDays.end()) return {}; // No dry day available, flood!
                ans[*it] = lake; // Assign this dry day to dry the current lake
                dryDays.erase(it); // Remove this dry day from available set
            }
            full[lake] = i; // Mark this lake as full today
            ans[i] = -1; // Raining, can't dry
        } else {
            dryDays.insert(i); // This is a dry day, can use it later
            // ans[i] stays 1 unless assigned to a specific lake above
        }
    }
    return ans;
}
};