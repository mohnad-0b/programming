import numpy as np
A = input()
A = A.split(" ")
my_array = np.array(A,dtype = int) # or A = [int(A[i]) for i in range(len(A))]
print(my_array.reshape(3,3))
