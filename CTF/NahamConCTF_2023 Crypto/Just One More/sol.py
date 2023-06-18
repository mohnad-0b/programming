from z3 import *

arr = eval(open('output.txt', 'r').read().split('\n')[0])
arr_s = eval(open('output.txt', 'r').read().split('\n')[1])

s = Solver()

# flag length 38
flag = [Int(f'flag_{i}') for i in range(38)]

s.add(flag[0] == ord('f'))
s.add(flag[1] == ord('l'))
s.add(flag[2] == ord('a'))
s.add(flag[3] == ord('g'))
s.add(flag[4] == ord('{'))
s.add(flag[-1] == ord('}'))

for i in range(5, len(flag) - 1):
    s.add(Or(And(flag[i] >= ord('a'), flag[i] <= ord('f')), And(flag[i] >= ord('0'), flag[i] <= ord('9'))))

for i in range(37):
    s.add(Sum([arr[j] * flag[j] for j in range(38)]) == arr_s[i])
    arr = [arr[-1]] + arr[:-1]


if s.check() == sat:
    m = s.model()
    print('flag: ', end='')
    print(''.join([chr(m[flag[i]].as_long()) for i in range(38)]))
else:
    print('unsat')

# flag{aad9ba9b3fdfa4cc6f7e2e18d0dcbbab}
