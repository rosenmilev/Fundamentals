def multiplication_sign(n1, n2, n3):
    minus_signs = 0
    zero = False

    for a in [n1, n2, n3]:
        if a < 0:
            minus_signs += 1

        if a == 0:
            zero = True

    if zero:
        result = "zero"

    else:
        if minus_signs % 2 == 0:
            result = "positive"

        else:
            result = "negative"

    return result


a1 = int(input())
a2 = int(input())
a3 = int(input())

print(multiplication_sign(a1, a2, a3))
