from collections import Counter
def solution(s):

    dic=Counter(s)
    cnt=0
    for val in dic.values():
        if val%2==1:
            cnt+=1

     
    
    return False if cnt >1 else True   
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
