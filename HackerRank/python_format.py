def print_formatted(number):

    w = len((bin(number))[2:])
    for i in range(number) : 
        print(f"{str(i+1).rjust(w)} {str(oct(i+1)[2:]).rjust(w)} {str(hex(i+1)[2:]).rjust(w).upper()} {str(bin(i+1)[2:]).rjust(w)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)