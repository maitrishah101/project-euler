def smallest_multiple(num):
    smallest_mult = num
    while divisible_by_term(num, smallest_mult) == False:
        smallest_mult += 10
    return smallest_mult

#checks to see if all the numbers up until term
#are divisible by n
def divisible_by_term(term, n):
    for i in range(2,term+1):
        if n % i != 0:
            return False
    return True

