def lucky42(nums):
    index = 0
    add = 0
    if nums[0] == 42:
        nums[0] -= 42
    for i in nums:
        if i == 42:
            nums[index] -= nums[index]
            nums[index-1] -= nums[index-1]
        index += 1
    for i in nums:
        add += i
    return add


a = lucky42([42, 2, 42, 3, 42, 4, 10, 999, 42, 1])
print(a)
