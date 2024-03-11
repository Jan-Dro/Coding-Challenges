
def letterCombinations(digits):
    if not digits:
        return []

    combos = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    result = [""]

    for digit in digits:
        new_combinations = []
        for combo in result:
            for letter in combos[digit]:
                print(letter)
                new_combinations.append(combo + letter)
        result = new_combinations

    return result
print(letterCombinations("23"))


        