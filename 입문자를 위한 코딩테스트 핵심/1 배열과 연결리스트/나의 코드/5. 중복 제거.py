\
def solution(nums):
    arr=[]
    arr.append(nums[0])
    for i in range(1,len(nums)):
        if nums[i]!=arr[-1]:
            arr.append(nums[i])
    arr.sort(reverse=True)
    
    return arr
    
   
print(solution([0, 1, 1, 1, 2, 2, 2, 3]))
print(solution([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5]))
print(solution([0, 0, 0, 3, 3, 3, 5, 7, 7, 7]))
print(solution([1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]))
