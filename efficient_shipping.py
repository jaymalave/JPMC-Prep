boxes = [3, 1, 6]
unitsPerBox = [2, 7, 4]
truckSize = 9

res = {}

for units in unitsPerBox:
    for box in boxes:
        res[units] = box
        boxes.remove(box)
        break

sorted_res = {}

for key, val in (sorted(res.items(), reverse=True)):
    sorted_res[key] = val 

#incomplete

        





     
    
