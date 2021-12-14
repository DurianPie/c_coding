#include<iostream>
#include<map>
using namespace std;
int last_ascii[200];
int vis_ascii[200];
int main()
{
    int n;
    char a;
    cin >> n;
    int cnt = 0;
    int last = 0, maxlen = 0, ans = 1;
    getchar();
    while(cnt < n)
    {
        a = getchar();
        if(!vis_ascii[int(a)] || last_ascii[int(a)] < last)
        {
            vis_ascii[int(a)] = 1;
            maxlen++;
            last_ascii[int(a)] = cnt;
            ans = max(ans, maxlen);
        }
        else
        {
            last = last_ascii[int(a)] + 1;
            last_ascii[int(a)] = cnt;
            maxlen = cnt + 1 - last;
        }
        cnt++;
    }
    cout<<ans<<endl;
    return 0;
}