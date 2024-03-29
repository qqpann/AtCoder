#include <bits/stdc++.h>
using namespace std;

vector<long long> enum_divisors(long long N)
{
    vector<long long> res;
    for (long long i = 1; i * i <= N; ++i)
    {
        if (N % i == 0)
        {
            res.push_back(i);
            // 重複しないならば i の相方である N/i も push
            if (N / i != i)
                res.push_back(N / i);
        }
    }
    // 小さい順に並び替える
    sort(res.begin(), res.end());
    return res;
}

int main(int argc, char *argv[])
{
    long long N;
    cin >> N;
    const vector<long long> &res = enum_divisors(N);
    for (int i = 0; i < res.size(); ++i)
        cout << res[i] << " ";
    cout << endl;
}
