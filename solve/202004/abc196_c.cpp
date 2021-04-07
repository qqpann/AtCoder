#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll n;
    cin >> n;
    string s = to_string(n);

    ll ans = 0;
    if (s.size() % 2 == 0)
    {
        ll tens = pow(10, s.size() / 2);
        ll left = n / tens;
        ll right = n % tens;
        if (left > right)
            ans--;
        ans += left - (tens / 10) + 1;
        ans += pow(10, (s.size() - 2) / 2) - 1;
    }
    else
    {
        ans += pow(10, (s.size() - 1) / 2) - 1;
    }
    cout << ans << endl;
}