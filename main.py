def plusOne(digits):

    numStorage = ''

    for number in digits:
        numStorage += str(number)

    numStorage = str(int(numStorage) + 1)
    answer = []

    for number in numStorage:
        answer.append(int(number))

    return answer


print(plusOne([9]))