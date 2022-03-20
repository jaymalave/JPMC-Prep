arr = list(map(int, input().split()))
new_arr = sorted(arr)

diff_arr = []

for i in range(len(new_arr) - 1):
    diff_arr.append(new_arr[i+1] -  new_arr[i])

min_diff = min(diff_arr)

min_diff_index = diff_arr.index(min(diff_arr))


for i in range(len(arr) - 1):
    if (new_arr[i+1] - new_arr[i]) == min_diff:
        print(min(new_arr[i+1], new_arr[i]), max(new_arr[i+1], new_arr[i]))


