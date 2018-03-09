def sum_primes(num):
    result = 0
    for i in range(2, num):
        if is_prime(i):
            result += i
    return result

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False
    for i in range(2,(num//2) + 1):
        if num % i == 0:
            return False
    return True

