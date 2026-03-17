# Удасться ли спрятать круглый коврик под прямоугольным ковриком?
# 1. Найдите диаметр круга
# # Если известен R радиус, то D = 2 * R
#
w, h, r = map(int, input("Введите три числа через пробел: ").split())
circle_diameter = 2 * r
# # Прямоугольник со сторонами a > D, b > D
# # Круг помещается свободно.
if circle_diameter <= min(w, h):
    print("Yes")
else:
    print("No")

w, h, r = map(float, input().split())
circle_diameter = 2 * r
if circle_diameter <= min(w, h):
    print("YES")
else:
    print("NO")