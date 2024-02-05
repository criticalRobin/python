def invert(lst):
    invert_nums = []

    if not lst:
        return []

    for num in lst:
        if num == 0:
            invert_nums.append(0)
        if num > 0:
            invert_nums.append(num - (num * 2))
        if num < 0:
            invert_nums.append((num - num) - num)
    return invert_nums


print(invert([1, -2, 3, -4, 5]))
