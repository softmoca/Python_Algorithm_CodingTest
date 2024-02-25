def solution(moves):
    x = y = 0

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    d=1

    for w in moves:
        if w=='G':
            x=x+dx[d]
            y=y+dy[d]
        elif w=='R':
            d=(d+1)%4
        elif w=='L':
            d=(d+3)%4
    

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
