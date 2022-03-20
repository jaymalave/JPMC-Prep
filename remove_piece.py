def winner(arr):
    i = 1
    a = 0
    b = 0

    while(i < len(arr)-1):
        if(arr[i-1] == arr[i] and arr[i] == arr[i+1]):
            if arr[i] == 'A':
                a += 1
            else:
                b += 1
        i += 1
    return a>b

arr = 'AAABABB'
print(winner(arr))
