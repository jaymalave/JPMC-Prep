arr = list(map(float, input().split()))

sum_arr = []
s = 0

for i in range(0, len(arr)):
    s = s + arr[i]
    sum_arr.append(s)

print(sum_arr)

print(min(sum_arr))

print(abs(min(sum_arr)) + 1)





