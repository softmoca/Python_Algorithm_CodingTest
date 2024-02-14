arr=[]

for _ in range(5):
    arr.append(int(input()))

avg=sum(arr)//5
arr.sort()
midd=arr[2]

print(avg)
print(midd)

