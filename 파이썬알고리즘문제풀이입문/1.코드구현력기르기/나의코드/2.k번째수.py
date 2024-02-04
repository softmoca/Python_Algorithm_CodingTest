T=int(input())


for i in range(T):
    n,s,e,k=map(int,input().split())
    arr=list(map(int,input().split()))
    temp=arr[s-1:e]
    temp.sort()
    print('#',i+1 , temp[k-1])










