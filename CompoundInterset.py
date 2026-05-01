P= int(input())
R=int(input())
T=int(input())
Amount=P*(1+R/100)**T
CI=Amount-P
print(f"{CI:.2f}")