from math import ceil

def merge_the_tools(string, k):
    # your code goes here
    cont = 0
    for i in range(ceil(len(string)/k)):
        s = string[cont:(cont + k)].split()
        s=list(dict.fromkeys(s[0]))
        s="".join(s)
        print(s)
        cont = cont + k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)