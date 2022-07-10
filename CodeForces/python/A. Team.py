number_of_problem=int(input())

solution=0

for i in range(number_of_problem):

        p = input().split(" ")
        if (int(p[0])+int(p[1])+int(p[2])) >= 2:
            solution += 1

print(solution)