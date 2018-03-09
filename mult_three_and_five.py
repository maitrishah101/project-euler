
def mult_three_and_five(num):
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


