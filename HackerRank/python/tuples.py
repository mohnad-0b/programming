from sympy import content

tuples=()
counter=int(input())
added_value=(input()).split()

for i in range(counter) :
    
    added_value_tuple = (int(added_value[i]),)
    tuples = tuples + added_value_tuple
print(tuples)
# print(hash(tuples))
