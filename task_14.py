# Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

import math

number1, number2 = map(int, input().split())
print(math.lcm(number1, number2))
