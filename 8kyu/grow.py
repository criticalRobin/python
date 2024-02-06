def grow(arr):
    ans = 1

    for num in arr:
        ans *= num
    return ans


print(grow([4, 1, 1, 1, 4]))
