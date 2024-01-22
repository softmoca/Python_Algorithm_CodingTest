def solution(moves):
    x = y = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    d=1
    for z in moves:
        if z=='G':
            x=x+dx[d]
            y=y+dy[d]
        elif z=='R':
            d=(d+1)%4
        elif z=='L':
            d=(d+3)%4

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
