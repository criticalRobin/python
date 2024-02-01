def square_up(n):
    result = []
    for i in range(1, n + 1):

        for j in range(n - i):
            result.append(0)

        for k in range(i, 0, -1):
            result.append(k)
        print(i)
    return result



print(square_up(3))
