#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll n;
    cin >> n;
    vector<ll> a(n), b(n);
    ll ans = pow(10, 5) * 2 + 1;
    for (ll i = 0; i < n; ++i)
        cin >> a.at(i) >> b.at(i);

    for (ll i = 0; i < n; ++i)
    {
        for (ll j = 0; j < n; ++j)
        {
            if (i == j)
                ans = min(ans, a.at(i) + b.at(j));
            else
                ans = min(ans, max(a.at(i), b.at(j)));
        }
    }
    cout << ans << endl;
}