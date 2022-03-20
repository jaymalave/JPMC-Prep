# def superReduced1(str):
#     new_str = str
#     count = 0
#     i = 0
#     while(i < (len(new_str) - 1)):
#         if(new_str[i] == new_str[i+1]):
#             count += 1
#             new_str.replace(new_str[i], "")
#             new_str.replace(new_str[i+1], "")
#             break
#         i += 1
#     if len(new_str) != 0 and count != 0:
#         superReduced1(new_str)
#     elif len(new_str) == 0: 
#         return "Empty string"
#     elif count == 0:
#         return new_str


def superReduced2(str):
    changed = True
    while changed and str != "":
        changed = False
        for i in range(len(str)-1):
            if str[i] == str[i+1]:
                changed = True
                str = str[:(i)] + str[(i+2):]
                break
    if str == "":
        return "Empty String"
    else:
        return str
            



print(superReduced1('baaba'))