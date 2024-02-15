def product_sans_n(nums):
    total_product = 1
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num

    products = []

    for num in nums:
        if zero_count > 1:
            products.append(0)
        elif zero_count == 1:
            if num == 0:
                products.append(total_product)
            else:
                products.append(0)
        else:
            products.append(total_product // num)

    return products
