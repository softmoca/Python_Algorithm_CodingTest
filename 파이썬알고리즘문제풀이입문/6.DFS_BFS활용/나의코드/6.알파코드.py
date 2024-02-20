def DFS(L):
    if L==len(arr):
        print(res)
    else:
        for i in range(len(arr)):
            for j in range(27):
                if arr[i]==j

        for i in range(27):
            if i<10:
                res[L]=i
                DFS(L+1)


arr=list(map(int,input()))

print(arr)


res=[]

DFS(0)
