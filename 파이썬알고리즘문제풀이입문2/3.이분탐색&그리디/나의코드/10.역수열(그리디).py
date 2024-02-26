
n=int(input())

arr=list(map(int,input().split()))
print(len(arr))
arr.insert(0,0)
ch=[0]*(n+1)



print(len(arr))
print()
for i in range(1,n+1):
    print(i)
    for j in range(arr[i],n+1):
        if ch[j]==0:
            ch[j]=i
            break

print(ch)




