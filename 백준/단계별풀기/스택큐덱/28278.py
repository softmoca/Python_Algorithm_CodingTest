import sys

N=int(input())
stack=[]
for _ in range(N):
    arr=list(map(int,sys.stdin.readline().split()))
    if len(arr)==1:
        if arr[0]==2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        if arr[0]==3:
            print(len(stack))
        if arr[0]==4:
            if stack:
                print(0)
            else:
                print(1)
        if arr[0]==5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        stack.append(arr[1])









