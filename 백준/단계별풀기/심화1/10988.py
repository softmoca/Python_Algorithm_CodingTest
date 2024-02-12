arr=list(map(str,input()))

n=len(arr)

for i in range(n//2):
    if arr[i]!=arr[-1-i]:
        print(0)
        break
else:
    print(1)    





