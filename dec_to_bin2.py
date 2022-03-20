def decToBin(n):
    if n > 1:
        decToBin(n//2)
    print(n%2, end = '')

decToBin(8)
print("\n")
