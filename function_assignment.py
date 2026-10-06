def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return f"{area:.2f}"


def taxes(money, tax):
    total = money + (money * tax)
    return total


def temperature(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


radius = float(input())
money = float(input())
tax = float(input()) / 100
fahrenheit = float(input())

print(circle_area(radius))
print(f"{taxes(money, tax):.2f}")
print(temperature(fahrenheit))