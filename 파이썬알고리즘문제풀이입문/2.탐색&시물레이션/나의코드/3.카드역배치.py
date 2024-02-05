arr=[]
for i in range(21):
    arr.append(i)


for _ in range(10):
    a,b=map(int,input().split())
    for i in range((b-a)//2+1):
        arr[a+i],arr[b-i]=arr[b-i],arr[a+i]
 

for i in range(1,21):
    print(arr[i],end=' ')

