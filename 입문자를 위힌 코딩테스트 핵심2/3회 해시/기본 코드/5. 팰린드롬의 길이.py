from collections import Counter
def solution(s):
    answer = 0
    dic=Counter(s)

    cnt=0
    for val in dic.values():
        if val%2==1:
            cnt+=1
        



    return len(s)-(cnt-1) if cnt>1 else len(s)
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
