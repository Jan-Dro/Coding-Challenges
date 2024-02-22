def sumOfAnArray(nums):
    answer = 0

    for num in nums:
        answer += num

    return answer

print(sumOfAnArray([1,2,3,4,5]))