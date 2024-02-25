def DFS(x,y,board):
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    board[x][y]=0
    global cnt
    cnt+=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<5 and 0<=ny<5 and board[nx][ny]==1:

            DFS(nx,ny,board)


global cnt
def solution(board):
    answer = []
    global cnt
    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                cnt=0
                DFS(i,j,board)
                answer.append(cnt)
    
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

