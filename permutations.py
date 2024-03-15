def permutations(nums):
    results = []
    def generate_permutations(start, end):
        if start == end:
            results.append(nums[:])

        else:
            for i in range(start, end):
                nums[start], nums[i] == nums[i], nums[start]
                generate_permutations(start + 1, end)
                nums[start], nums[i] == nums[i], nums[start]
    generate_permutations(0, len(nums))
    return results


print(permutations([1,2,3]))