def solution(s):
    answer = 'YES'
    stack=[]

    for x in s:
        if x=='(':
            stack.append(x)
        elif stack and x==')':
            stack.pop()
        elif len(stack)==0 and x==')':
            answer="NO"
        
    if len(stack)>0:
        answer="NO"

    return answer


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
