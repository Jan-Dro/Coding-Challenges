def rotate(nums, k):
    start = len(nums) -1
    k -= 1
    while k >= 0:
        rando = nums.pop(start)
        nums.insert(0, rando)
        k -= 1

    return nums

print(rotate([1,2,3,4,5,6,7], 3))