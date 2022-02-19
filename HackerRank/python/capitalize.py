s = input() # don't need this line to solve challenge :) 
s = s.split(" ")

for i in range(len(s)):
    if s[i] == "" :
        continue # if s[i] is Empty dont do any thing
    elif not(s[i][0].isnumeric()) :
        s[i] = s[i].capitalize()
print(' '.join(s))
