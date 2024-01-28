def group(strs):
    answer = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))
        # print(word, '-----', sorted_word)
        if sorted_word in answer:
            answer[sorted_word].append(word)
        else:
            answer[sorted_word] = [word]
    return list(answer.values())


print(group(["eat","tea","tan","ate","nat","bat"]))