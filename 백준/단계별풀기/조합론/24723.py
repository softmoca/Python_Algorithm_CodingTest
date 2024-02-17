from itertools  import combinations

n,m=map(int,input().split())
arr=list(range(1,n+1))

arr2=list(combinations(arr,m))

print(len(arr2))





# def DFS(L,s):
#     global cnt
#     if L==m:
#         cnt+=1
#     else:
#         for i in range(s,n+1):
#             res[L]=i
#             DFS(L+1,i+1)



# n,m=map(int,input().split())
# res=[0]*(n+1)
# cnt=0
# DFS(0,1)
# print(cnt)



