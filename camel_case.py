def camelCase(str):
    count = 1
    for i in range(len(str)):
        if(65 <= ord(str[i]) <= 90):
            count += 1
    return count

print(camelCase("saveChangesInTheEditor"))


