def sum_array(arr):
    if not arr or len(arr) == 1:
        return 0
    return sum(arr) - min(arr) - max(arr)


print(sum_array([6, 2, 1, 8, 10]))
