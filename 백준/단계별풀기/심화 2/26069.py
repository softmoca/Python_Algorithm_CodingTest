

n=int(input())
arr=set()
arr.add('ChongChong')

for _ in range(n):
    a,b=input().split()
    if a in arr:
        arr.add(b)
    if b in arr:
        arr.add(a)



print(len(arr))
   



