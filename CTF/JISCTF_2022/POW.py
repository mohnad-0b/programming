import hashlib

chr = "" # prefix character

for i in range(1000000000000000000000000000):
    hashed_string = hashlib.sha256(( str(i)).encode('utf-8')).hexdigest()
    if chr == str(hashed_string)[:len(chr)]:
        print(hashed_string, str(i))
        break
