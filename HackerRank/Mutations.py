def mutate_string(string, position, character):
    string_new = string[:position] + character + string[position + 1:]
    return string_new

# another way
def mutate_string2(string, position, character) :
    string=" ".join(string)
    string = string.split()
    string[position] = character
    string="".join(string)
    return string    # print(string)