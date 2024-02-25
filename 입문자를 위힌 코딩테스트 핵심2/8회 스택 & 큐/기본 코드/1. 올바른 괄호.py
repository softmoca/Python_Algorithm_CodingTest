def solution(s):
    answer = "YES"


    stack=[]

    for x in s:
        if x=='(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                answer="NO"
                break
    if stack:
        answer='NO'
    

    return answer


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
