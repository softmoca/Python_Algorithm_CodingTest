n=int(input())

arr=list(map(int,input().split()))
arr2 = sorted(list(set(arr)))

dic=dict()
for i in range(len(arr2)):
    dic[arr2[i]]=i

for x in arr:
     print(dic[x], end = ' ')



#####################################
for i in range(n):
    for j in range(len(arr2)):
        if arr[i]==arr2[j]:
            print(j,end=' ')
            break

for x in arr:    
    print(arr2.index(x), end = ' ')
#####################################


