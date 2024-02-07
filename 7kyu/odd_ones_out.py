def odd_ones_out(numbers):
    pair_numbers = []

    for num in numbers:
        if (numbers.count(num) % 2) == 0:
            pair_numbers.append(num)

    return pair_numbers
