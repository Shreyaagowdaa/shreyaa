a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
D = (b ** 2) - (4 * a * c)
sol1 = -b - D ** 0.5 / 2 * a
sol2 = -b + D ** 0.5 / 2 * a
print("The roots of this quadratic equations are", sol1, "and", sol2)
