if islower(string[0]):
    for i in range(len(string[0:])-1):
        if  islower(string[i+1]):
            print(string)
            break
            #exit()
    if i == (len(string[0:])-2):
        print(string[0].upper()+string[1:].lower())
else :
    for i in range(len(string[0:])-1):
        if  islower(string[i+1]):
            print(string)
            break
            #exit()
    if i == (len(string[0:])-2):
        print(string.lower())
