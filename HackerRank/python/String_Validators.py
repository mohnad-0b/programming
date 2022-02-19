string = input() 

for i in range(len(string)) : 
    if string[i].isalnum(): 
        print(string[i].isalnum()) 
        break 
    elif i==(len(string)-1): 
        print(string[i].isalnum()) 

for i in range(len(string)) : 
    if string[i].isalpha(): 
        print(string[i].isalpha()) 
        break 
    elif i==(len(string)-1): 
        print(string[i].isalpha()) 

for i in range(len(string)) : 
    if string[i].isdigit(): 
        print(string[i].isdigit()) 
        break 
    elif i==(len(string)-1): 
        print(string[i].isdigit()) 

for i in range(len(string)) : 
    if string[i].islower(): 
        print(string[i].islower()) 
        break 
    elif i==(len(string)-1): 
        print(string[i].islower()) 

for i in range(len(string)) : 
    if string[i].isupper(): 
        print(string[i].isupper()) 
        break 
    elif i==(len(string)-1): 
        print(string[i].isupper())