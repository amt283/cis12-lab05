def decimal_to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    next, digit = divmod(n, 2)
    result = decimal_to_binary(next)
    return decimal_to_binary(next) + str(digit)

def binary_to_decimal(b):
    if b == '':
        return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))

print(decimal_to_binary(100))

print(binary_to_decimal('1100100'))