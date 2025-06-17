#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;
using ll = long long;

ll modExp(ll base, ll exp) {
    ll result = 1;
    ll cur = base % MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * cur) % MOD;
        cur = (cur * cur) % MOD;
        exp >>= 1;
    }
    return result;
}

// Precompute factorials and inverse factorials for nCr
const int MAX = 100000; // Should be >= n
ll fact[MAX+1], invFact[MAX+1];

ll modInv(ll a, ll m = MOD) {
    // Fermat's little theorem, since MOD is prime
    return modExp(a, m - 2);
}

void precomputeFactorials(int maxN) {
    fact[0] = 1;
    for (int i = 1; i <= maxN; ++i) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }
    invFact[maxN] = modInv(fact[maxN]);
    for (int i = maxN - 1; i >= 0; --i) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

ll nCr(int n, int r) {
    if (r > n || r < 0) return 0;
    return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
}

class Solution {
public:
    int countGoodArrays(int n, int m, int k) {
        // Edge cases
        if (k >= n) return 0;

        // Precompute factorials up to n-1
        precomputeFactorials(n);

        ll combinations = nCr(n - 1, k);
        ll powTerm = modExp(m - 1, n - k - 1);
        ll ans = (combinations * m) % MOD;
        ans = (ans * powTerm) % MOD;

        return (int)ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    Solution sol;
    cout << sol.countGoodArrays(n, m, k) << "\n";

    return 0;
}
