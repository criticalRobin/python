def max_product(lst, n_largest_elements):
    nums = []
    ans = 1

    for i in range(0, n_largest_elements):
        nums.append(max(lst))
        lst.remove(max(lst))

    for num in nums:
        ans *= num

    return ans
