class Solution {
public:
    string sortVowels(string s) {
        // Define vowels for easy checking
        string vowels = "aeiouAEIOU";
        vector<char> v;
        // Collect all vowels from the string
        for (char c : s) {
            if (vowels.find(c) != string::npos) v.push_back(c);
        }
        // Sort the vowels by ASCII value
        sort(v.begin(), v.end());
        int idx = 0;
        // Replace vowels in the original string with sorted vowels
        for (char &c : s) {
            if (vowels.find(c) != string::npos) c = v[idx++];
        }
        return s;
    }
};