def sum_array(a):
    sum = 0

    if len(a) == 0:
        return 0

    for val in a:
        if val > 0:
            sum += val
        else: 
            sum -= val
    
    return sum

print(sum_array([4, 5, 6]))