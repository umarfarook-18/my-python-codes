import math
X, Y = map(int, input().split())
hypotenuse = math.sqrt(X**2 + Y**2)
print(f"{hypotenuse:.2f}")