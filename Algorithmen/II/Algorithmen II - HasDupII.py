def hasDupII(numbers):
    already_seen_list = []
    for i in range(max(numbers)+1):
        already_seen_list.append(False)
    
    for x in range(0,len(numbers)):
        num = numbers[x]
        if already_seen_list[num] == True:
            return True
        else:
            already_seen_list[num] = True
    
    return False

numbers = [21,12,15,8,22,13,5,9,0,1,2,3,4,6,3,4]
result = hasDupII(numbers)
print("Has Duplicates:", result)

