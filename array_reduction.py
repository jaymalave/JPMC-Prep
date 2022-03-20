cost_arr = []

def reduceArray(arr):
   sorted_arr = sorted(arr)
   sorted_arr.append(sorted_arr[0] + sorted_arr[1])
   cost_arr.append(sorted_arr[0] + sorted_arr[1])
   sorted_arr.pop(0)
   sorted_arr.pop(0)
   if len(sorted_arr) > 1:
       reduceArray(sorted_arr)
   else:
        return cost_arr


arr = list(map(float, input().split()))

print(reduceArray(arr))

#incomplete




