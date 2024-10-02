def check (string:str) -> int:
    checkString = string.upper()

    count = 0
    for i in range(len(checkString)):
        if checkString[i] == 'A':
            count += 1
    
    return count

string = check("arara")
print(string)