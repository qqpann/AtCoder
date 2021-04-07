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

string solve_odd_even_divisors(vector<long long> vec)
{
    long long odd = 0;
    long long even = 0;
    for (long long i = 0; i < vec.size(); ++i)
    {
        if (vec.at(i) % 2 == 0)
            even++;
        else
            odd++;
    }

    if (odd > even)
        return "Odd";
    else if (even > odd)
        return "Even";
    else
        return "Same";
}

string solve(long long N)
{
    long long odd = 0;
    long long even = 0;

    for (long long i = 1; i * i <= N; ++i)
    {
        if (N % i == 0)
        {
            if (i % 2 == 0)
                even++;
            else
                odd++;

            // 重複しないならば i の相方である N/i も push
            if (N / i != i)
            {
                if ((N / i) % 2 == 0)
                    even++;
                else
                    odd++;
            }
        }
    }

    if (odd > even)
        return "Odd";
    else if (even > odd)
        return "Even";
    else
        return "Same";
}

int main(int argc, char *argv[])
{
    long long T;
    cin >> T;
    long long maximumN = 0;
    vector<long long> vec_case(T);

    for (long long i = 0; i < T; i++)
    {
        cin >> vec_case.at(i);
        if (vec_case.at(i) > maximumN)
            maximumN = vec_case.at(i);
    }

    vector<string> memo(maximumN + 1);

    for (long long i = 0; i < T; i++)
    {
        const string res = solve(vec_case.at(i));
        cout << res << endl;
    }
}
