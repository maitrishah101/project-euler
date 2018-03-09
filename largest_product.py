def largest_product(num, num_digits):
    result = 1
    max_result = 1
    while num > 10**(num_digits-1):
        for i in range(num_digits, 0, -1):
            number = str(num)
            result *= int(number[len(number)-i])
        if result > max_result:
            max_result = result
        num = num // 10
        result = 1
    return max_result

