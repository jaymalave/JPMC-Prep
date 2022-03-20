def binToDec(n):

    decimal, i = 0, 0
    while(n != 0): 
        dec = n % 10
        decimal = decimal  + dec * pow(2, i)
        n = n//10
        i += 1
    return decimal

print(binToDec(1000))
    