pairs=0

n = int(input()) # number of boys
a =  input().split(" ") # skill boys

m = int(input()) # number of girls
b =  input().split(" ") # skillgirls 

a.sort()
b.sort()

i=-1
maxi=len(a)*len(b)
maxlen = max(len(a),len(b))


if len(a) == len(b):
    maxi = len(a)

    while (True):
            i+=1

            if (len(a) != 0 and len(b) != 0 and i < maxi):
                # print(i%len(a),i%len(b),len(a),len(b),a[i],b[i])
                if ( abs(int(a[i%len(a)])-int(b[i%len(b)])) <= 1):

                    a.remove(a[i%len(a)])
                    b.remove(b[i%len(b)])
                    pairs += 1
                # else:
                #         if int(a[i%len(a)]) > int(b[i%len(b)]) :
                #             a.insert(0,int(b[i%len(b)]))
                #         else:
                #             b.insert(0,int(a[i%len(a)]))

            else:
                print(i,maxi)
                break

elif maxlen == len(b) :
    
    while (True):
        i+=1

        if (len(a) != 0 and len(b) != 0 and i < maxi):
            if ( abs(int(a[0])-int(b[i%len(b)])) <= 1):

                a.remove(a[0])
                b.remove(b[i%len(b)])
                pairs += 1
            elif i > maxlen:
                maxlen += maxlen
                a.remove(a[0])
        else:
            break
else:
    while (True):
        i+=1

        if (len(a) != 0 and len(b) != 0 and i < maxi):
            if ( abs(int(a[i%len(a)])-int(b[0])) <= 1):

                a.remove(a[i%len(a)])
                b.remove(b[0])
                pairs += 1
            elif i > maxlen:
                maxlen += maxlen
                b.remove(b[0])
        else:
            break

print(pairs)