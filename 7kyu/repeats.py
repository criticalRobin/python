def repeats(arr):
    sum = 0

    for num in arr:
        if arr.count(num) == 1:
            sum += num
        else:
            pass

    return sum
