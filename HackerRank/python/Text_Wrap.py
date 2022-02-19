import textwrap 
from math import ceil 
def wrap(string,maxwidth) : 
    j=0 
    result="" 
    for i in range(int(ceil(len(string)/maxwidth))) : 
        result= result + (string[(0+j):(maxwidth+j)]) + "\n" 
        j=j+maxwidth          
    return result 

if __name__ == '__main__': 
    string, max_width = input(), int(input()) 
    result = wrap(string, max_width) 
    print(result)
