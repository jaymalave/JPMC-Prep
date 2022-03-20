def marsCrash(message):
    count = 0
    for i, char in enumerate(message):
     if i%3 == 1:
        if char != 'O':
            count += 1
     else:
        if char != 'S':
            count += 1
    return count

print(marsCrash('SOSSPSSQSSOR'))


