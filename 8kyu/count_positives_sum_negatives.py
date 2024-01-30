def count_positives_sum_negatives(arr):
    counter = 0
    negative_sum = 0

    if len(arr) == 0:
        return []

    for num in arr:
        if num > 0:
            counter += 1
        else:
            negative_sum += num
    
    return [counter, negative_sum]

