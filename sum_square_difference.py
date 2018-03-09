def sum_square_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    while n > 0:
        sum_of_squares += (n ** 2)
        square_of_sum += n
        n -= 1
    return (square_of_sum ** 2) - sum_of_squares

