#include <bits/stdc++.h>
using namespace std;

int solve_line(string line, int p)
{
    int tmp_count = 0;
    bool passed = false;
    int N = line.size();
    for (int j = 1; j <= N; ++j)
    {
        if (j == p)
            passed = true;

        if (line.at(j - 1) == '.') // .
            tmp_count++;
        else if (!passed) // #
            tmp_count = 0;
        else
            break;
    }
    return tmp_count;
}

int main()
{
    int h, w, x, y;
    cin >> h >> w >> x >> y;
    string row;
    string col = "";
    int count = 0;
    // Scan each row (moving vertically)
    for (int i = 1; i <= h; ++i)
    {
        cin >> row;
        col += row.at(y - 1);
        if (i == x)
        {
            // Scan current row (moving horizontally)
            count += solve_line(row, y);
        }
    }
    count += solve_line(col, x) - 1; // do not double count
    cout << count << endl;
}