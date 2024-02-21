import sys

def DFS(x, y, n):
    global white, blue
    color = paper[x][y] # 첫 번째 색

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                DFS(x, y, n // 2)        # 1사분면
                DFS(x, y + n // 2, n // 2)      # 2사분면
                DFS(x + n // 2, y, n // 2)      # 3사분면
                DFS(x + n // 2, y + n // 2, n // 2)    # 4사분면
                return

    if color == 0:
        white += 1
    else:
        blue += 1

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white, blue = 0, 0
DFS(0, 0, n)

print(white)
print(blue)



