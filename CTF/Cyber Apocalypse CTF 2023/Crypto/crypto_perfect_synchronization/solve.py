from string import ascii_uppercase

key = {}
out = open('output.txt').read().splitlines()
for i in out:
    print(i)
    if i == 'fbe86a428051747607a35b44b1a3e9e9':
        key[i] = '{'
    elif i == 'c53ba24fbbe9e3dbdd6062b3aab7ed1a':
        key[i] = '}'
    elif i == '61331054d82aeec9a20416759766d9d5':
        key[i] = ' '
    elif i == '5ae172c9ea46594cea34ad1a4b1c79cd':
        key[i] = '_'
    elif i not in key:
        key[i] = ascii_uppercase[0]
        ascii_uppercase = ascii_uppercase[1:]

for i in out:
    print(key[i], end='')

# use https://quipqiup.com/ flag is HTB{AJSIMPLEJSUBSTITUTIONJISJWEAK}