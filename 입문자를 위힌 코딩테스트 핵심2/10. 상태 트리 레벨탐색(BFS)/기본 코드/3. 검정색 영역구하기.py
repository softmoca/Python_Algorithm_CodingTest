from collections import deque
def solution(board):
    answer = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    dq=deque()

    for i in range(5):
        for j in range(5):
            if board[i][j]==1:
                answer+=1
                dq.append([i,j])
                board[i][j]=0
                while dq:
                    for _ in range(len(dq)):
                        x,y=dq.popleft()

                        for k in range(4):
                            nx=x+dx[k]
                            ny=y+dy[k]
                            if 0<=nx<5 and 0<=ny<5 and board[nx][ny]==1:
                                board[nx][ny]=0
                                dq.append([nx,ny])

                        

    
    return answer
            
print(solution([[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[1, 1, 1, 0, 1], [1, 1, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 0]]))
print(solution([[0, 0, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 0, 0]]))

