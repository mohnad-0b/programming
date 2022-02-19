# better solve
n = input() # not useful
List = input()
List =  List.split(" ")
List = list(dict.fromkeys(List))
for i in range(len(List)) :
    List[i] = int(List[i])
List.sort()
print(List[-2])

# if __name__ == '__main__':
#     n = int(input())
#     arr = input().split()
#     max = arr[0]
#     # print(arr)

#     for i in range(0,n) :
#         if int(max) < int(arr[i]) :
#             # print(f"{max} < {arr[i]}")
#             # print(f"(${arr[i]}) max = ${max}")
#             max = arr[i]
#             # print(f"(${arr[i]}) max = ${max}")

#         # elif  (i+1) == n :
#             # print(f"else\nmax = ${max}\n${'#'*25}")
    
#     arr = set(arr)
#     arr = list(arr)
#     arr.remove(max)
#     #print(arr)
#     n = len(arr)
#     max = arr[0]


#     for i in range(0,n) :
#         if int(max) < int(arr[i]) :
#             max = arr[i]
#             # print(f"max = ${max}")
#         #elif  (i+1) == n :
#     print(max)            # print(f"max = ${max}")
    
    

