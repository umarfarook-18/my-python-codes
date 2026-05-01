A, B = map(int, input().split())
for n in range(A + 1, B):
    square = n ** 2
    cube = n ** 3
    print(n, square, cube)