def count_substring(string, sub_string) :
    c=0
    index=0
    while (string.find(sub_string,index) != -1) :
        c = c + 1
        index=string.find(sub_string,index)+1
    else :
        return c
        