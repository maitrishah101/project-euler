def nth_prime(n):
    nth_prime_num = 1
    first_prime = 2
    while nth_prime_num != n:
        find_next_prime()
        nth_prime_num += 1

def make_find_next_prime():
    first_prime_num = 2
    def find_next_prime():
        nonlocal first_prime_num
        while not is_prime():
            first_prime_num += 1
        return first_prime_num
    return find_next_prime


