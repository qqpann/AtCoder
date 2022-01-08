#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define REP(i, m, n) for (ll i = (ll)(m); i < (ll)(n); i++)
#define rep(i, n) REP(i, 0, n)

int main()
{
    string n;
    cin >> n;
    n.erase(find_if(n.rbegin(), n.rend(), [](unsigned char c) {
        return c != '0';
    }));

    // reverse(n.begin(), n.end());
}