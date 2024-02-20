import sys
  

n=int(input())
bricks=[]
for i in range(n):
    a, b, c=map(int, input().split())
    bricks.append((a, b, c))

bricks.sort(reverse=True)

dy=[0]*n # 해당 인덱스의 벽돌이 최상단에 올떄의 높이 값 
dy[0]=bricks[0][1]



for i in range(1, n):
    max_h=0;
    for j in range(i-1, -1, -1):
        if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
            max_h=dy[j]
    dy[i]=max_h+bricks[i][1]
print(max(dy))










