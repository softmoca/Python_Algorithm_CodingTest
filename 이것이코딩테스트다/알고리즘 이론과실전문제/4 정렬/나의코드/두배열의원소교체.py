n,k=map(int,input().split())


arrA=list(map(int,input().split()))
arrB=list(map(int,input().split()))
arrA.sort()
arrB.sort(reverse=True)

for i in range(k):
    arrA[i],arrB[i]=arrB[i],arrA[i]


print(sum(arrA))