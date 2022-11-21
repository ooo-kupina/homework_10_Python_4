from numpy.polynomial import Polynomial as P
from random import randint

def polynom1(k1):

    set1 = [randint(0, 100) for i in range(k1 + 1)]

    # print(f"Список коэффициентов многочлена №1: {set1}")

    p1 = P(set1)

    # print(f"Многочлен №1 = {p1}")

    poly_1 = p1

    return poly_1

def polynom2(k2):

    set2 = [randint(0, 100) for i in range(k2 + 1)]

    # print(f"Список коэффициентов многочлена №2: {set2}")

    p2 = P(set2)

    # print(f"Многочлен №2 = {p2}")

    poly_2 = p2

    return poly_2


def poly_sum(p1, p2):

    sum_poly = p1 + p2

    print(f"Сумма многочленов №1 и №2 = {sum_poly}")

    return sum_poly

# k1 = 5
# k2 = 4
#
# set1 = [randint(0, 100) for i in range(k1 + 1)]
# set2 = [randint(0, 100) for j in range(k2 + 1)]
#
# print(f"Список коэффициентов многочлена №1: {set1}")
# print(f"Список коэффициентов многочлена №2: {set2}")
#
# p1 = P(set1)
# p2 = P(set2)
#
# print(f"Многочлен №1 = {p1}")
# print(f"Многочлен №2 = {p2}")
#
# print(f"Сумма многочленов №1 и №2 = {p1} + {p2}")