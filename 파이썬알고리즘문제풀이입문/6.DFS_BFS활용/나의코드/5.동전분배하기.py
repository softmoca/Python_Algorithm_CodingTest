
def DFS(L):
    global Minn
    if L==n:
        if ch[0]!=ch[1] and ch[1]!=ch[2] and ch[0] != ch[2]:
            tmp=max(ch)-min(ch)
            if tmp<Minn:
                print(ch)
                Minn=tmp
    else:
        for i in range(3):
            ch[i]+=arr[L]
            DFS(L+1)
            ch[i]-=arr[L]
            
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
ch=[0]*3
Minn=100000
DFS(0)
print(Minn)