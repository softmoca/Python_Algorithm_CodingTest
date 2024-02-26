


n=int(input())
res=[]

arr=[list(map(int,input().split())) for _ in range(n) ]

summ=0
for i in range(n//2):
    summ=summ+sum(arr[i][  n//2 -i  :  n//2 +1 +i ])

summ=summ+sum(arr[n//2])

for i in range(n//2):
    summ=summ+sum(arr[-(i+1)][    n//2 -i  :  n//2 +1 +i ])

print(summ)