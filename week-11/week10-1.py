n, m = map(int, input().split())
cards = input()
cnt = [0] * 26
for i in range(len(cards)):
    cnt[ord(cards[i]) - ord('A')] += 1
cnt.sort(reverse=True)
selected_m, ans = 0, 0
for i in range(26):
    if m - selected_m >= cnt[i]:
        selected_m += cnt[i]
        ans += cnt[i] * cnt[i]
    else:
        ans += (m - selected_m) * (m - selected_m)
        break
print(ans)
'''
5 5
MJDIJ

'''
