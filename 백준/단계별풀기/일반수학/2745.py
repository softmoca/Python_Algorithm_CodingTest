a,b=map(str,input().split())
arr=list(map(str,a))
n=int(b)
S=0

for i in range(len(arr)):
    if arr[i].isdecimal():
        x=int(arr[i])
    else:
        x=ord(arr[i])-55
    for _ in range(len(arr)-i-1):
        x=x*n
    S+=x
print(S)






