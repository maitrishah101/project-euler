def even_fib_numbers():
    sum = 2
    first_fib = 1
    second_fib = 2

    while first_fib + second_fib < 4000000:
        if (first_fib + second_fib) % 2 == 0:
            sum += first_fib + second_fib
        temp = first_fib
        first_fib = second_fib
        second_fib = first_fib + temp
        
    return sum

