arr=[[-1]*5 for _ in range(5)]
arr=[list(map(str,input())) for _ in range(5)]
M=0
for i in range(5):
    if len(arr[i])>M:
        M=len(arr[i])


for i in range(5):
    if len(arr[i])!=M:
        for _ in range(M-len(arr[i])):
            arr[i].append(-1)

for i in range(M):
    for j in range(5):
        if arr[j][i]!=-1:
            print(arr[j][i],end='')


