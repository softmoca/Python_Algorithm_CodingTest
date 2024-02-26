# n,w=map(int,input().split())


# arr=list(map(int,input().split()))
# res=[]
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             res.append(arr[i]+arr[j]+arr[k])

# S=list(set(res))
# S.sort(reverse=True)

# print(S[w-1])

from itertools import combinations

n,k=map(int,input().split())

res=[]
arr=list(map(int,input().split()))
res1=list(combinations(arr,3))
for x in res1:
    print(x)
    res.append(sum(x))

S=list(set(res))
S.sort(reverse=True)

print(S[k-1])






