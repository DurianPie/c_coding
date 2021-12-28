/* 距离产生美

4
0 20 30 50
20 0 50 15
30 50 0 20
50 15 20 0

*/
#include<iostream>
#include<cmath>
using namespace std;

int n, dist[20][20], div_m[20];

int sum_div()
{
    int ans = 0;
    for(int i = 0; i < 20; i++)
        ans += div_m[i];
    return ans;
}

int cal()
{
    int ans = 0;
    for(int i = 0; i < n; i++)
        if(div_m[i] == 0)
            for(int j = 0; j < n; j++)
                if(div_m[j] == 1)
                    ans += dist[i][j];
    return ans;
}

int dfs(int n, int i)
{
    int ans = 0;
    if(i == n-1)
    {
        if(sum_div() != 0)
            ans = max(ans, cal());
        if(sum_div() != n-1)
            ans = max(ans, cal());
    }
    else
    {
        ans = max(ans, dfs(n, i+1));
        div_m[i] = 1;
        ans = max(ans, dfs(n, i+1));
        div_m[i] = 0;
    }
    return ans;
}

int main()
{
    cin >> n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            cin >> dist[i][j];
    int ans = 0;
    ans = dfs(n, 0);
    cout << ans;
    return 0;
}
