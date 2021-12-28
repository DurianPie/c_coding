#include<iostream>
#include<algorithm>
using namespace std;
struct item
{
    int a,b;
    /* data */
};



int main()
{
    int n;
    cin>>n;
    int nums[2010][2];
    for(int i=0; i<n; i++)
    {
        cin>>nums[i][0];
        nums[i][1] = i;
    }
    nums.sort()
    // # print(nums)
    ans = 0
    for i in range(n-1, -1, -1):
        # print(i)
        pre_num, behind_num = 0, 0
        for j in range(0, i):
            if nums[j][0] < nums[i][0]:
                if nums[j][1] > nums[i][1]:
                    behind_num += 1
                else:
                    pre_num += 1
        ans += min(pre_num, behind_num)
    print(ans)
    return 0;
}