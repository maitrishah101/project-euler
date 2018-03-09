from math import sqrt
def is_prime_num(n):
    if n % 2 == 0:
        return False
    else:
        div = n // 2
        while div > 1:
            if n % div == 0:
                return False
            div -= 1
    return True


def largest_prime_factor(num):
    largest_prime_fact = (sqrt(num) // 1) * 2
    while largest_prime_fact > 0:
        if num % largest_prime_fact == 0 and is_prime_num(largest_prime_fact):
            return largest_prime_fact
        else:
            largest_prime_fact -= 1


