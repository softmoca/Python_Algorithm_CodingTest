import sys

def DFS(x,y,n):
    check=arr[x][y]
    global k1,k2,k3
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=check:
                DFS(x,y,n//3)
                DFS(x,y+n//3,n//3)
                DFS(x,y+n//3+n//3,n//3)
                DFS(x+n//3,y,n//3)
                DFS(x+n//3,y+n//3,n//3)
                DFS(x+n//3,y+n//3+n//3,n//3)
                DFS(x+n//3+n//3,y,n//3)
                DFS(x+n//3+n//3,y+n//3,n//3)
                DFS(x+n//3+n//3,y+n//3+n//3,n//3)
                return
    
    if check==-1:
        k1+=1
    elif check ==0:
        k2+=1
    elif check ==1:
        k3+=1



n=int(input())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n) ]

k1,k2,k3=0,0,0
DFS(0,0,n)

print(k1,k2,k3,sep='\n')

