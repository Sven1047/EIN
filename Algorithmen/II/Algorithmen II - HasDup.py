def hasDup(numbers):
    for x in range(0,len(numbers)):
        for y in range(0,len(numbers)):
            if numbers[x] == numbers[y] and x!=y:
                return True
    return False

numbers = [21,12,15,8,22,13,5,9,0,1,2,3,4,6,3,4]
result = hasDup(numbers)
print("Has Duplicates:", result)

