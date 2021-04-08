#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll n;
    cin >> n;
    ll th = 1000;
    ll commas = 1;

    ll count = 0;
    while (n >= th)
    {
        if (n >= th * 1000)
        {
            count += (th * 1000 - th) * commas;
        }
        else
        {
            count += (n - th + 1) * commas;
        }
        th = th * 1000;
        commas ++;
    }
    cout << count << endl;
}