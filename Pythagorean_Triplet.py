def pythagorean_triplet(num):
    a = 8
    b = 15
    c = 17
    a_1, b_1, c_1 = 0,0,0
    total = a + b + c
    mult = 2
    while total != num:
        a_1 = a*mult
        b_1 = b*mult
        c_1 = c*mult
        total = a_1 + b_1 + c_1
        mult += 1
    return a_1 * b_1 * c_1

