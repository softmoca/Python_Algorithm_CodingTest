m = int(input())
n = int(input())

ch = [0] * (n + 1)  


for i in range(2, int(n ** 0.5) + 1):
    if ch[i] == 0:
        for j in range(i * i, n + 1, i):
            ch[j] = 1  

res = []


for i in range(max(2, m), n + 1):
    if ch[i] == 0:
        res.append(i)


if len(res) > 0:
    print(sum(res))
    print(min(res))
else:
    print(-1)
