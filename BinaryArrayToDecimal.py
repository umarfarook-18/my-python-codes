N = int(input())
nums = list(map(int,input().split()))
decimal = 0
for i in range(N):
    decimal += nums[i] * (2 ** (N - 1 - i))
print(decimal)