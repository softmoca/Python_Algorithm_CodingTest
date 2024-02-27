
    
n,m=map(str,input().split())
m=int(m)
stack=[]
for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m=m-1
    stack.append(x)

if m:
    for _ in range(m):
        stack.pop()

for x  in stack:
    print(x,end='')



