T=int(input())

for _ in range(1,T+1):
    n,s,e,k=map(int,input().split())
    arr=list(map(int,input().split()))
    tmp=arr[s-1:e]
    tmp.sort()
    print(f'#{T} {tmp[k-1]}'  )









