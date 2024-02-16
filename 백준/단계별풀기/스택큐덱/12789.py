

n=int(input())

arr=list(map(int,input().split()))


stack=[]

for i in range(n):
    if arr[i]!=min(arr[i:]):
        stack.append(arr[i])

for _ in range(len(stack)):
    if len(stack)>1:
        if stack[-1]<stack[-2]:
            stack.pop()
    elif len(stack)==1:
        stack.pop()




if not stack: 
    print('Nice')
else:
    print('No')


