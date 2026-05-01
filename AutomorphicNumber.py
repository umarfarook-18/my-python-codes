n = int(input())
square = n * n
if str(square).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")