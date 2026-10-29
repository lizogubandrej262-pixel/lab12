def count_even(num):
    count = 0
    for digit in str(num):
        d = int(digit)
        if d % 2 == 0:
            count = count + 1
    return count


def product_odd(num):
    product = 1
    has_odd = False
    for digit in str(num):
        d = int(digit)
        if d % 2 != 0:
            product = product * d
            has_odd = True
    if has_odd == False:
        return 0
    return product  