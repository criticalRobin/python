def cat_jumps(start, finish):
    jumps = 0

    while start < finish:
        if (finish - start) >= 3:
            jumps += 1
            start += 3
        
        if (finish - start) == 2:
            jumps += 2
            start += 2

        if (finish - start) == 1:
            jumps += 1
            start += 1
    return jumps


print(cat_jumps(3, 6))        
        