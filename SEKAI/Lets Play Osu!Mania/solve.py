N = int(input())
body = []
c = 0
hold_note = []
for i in range(N):
    body.append(input().split('\n'))
# print(body)
for i in range(len(body)):
    # print(len(i[0]))
    for j in range(6):
        if (body[i][0][j] == "-") and (body[(i+1)%len(body)][0][j] != "#"):
            c += 1
        # if (body[i][0][j] == "#")/:
            # hold_note.append(j)

# output = []
# for x in range(0,len(hold_note)-1):
#     # if (hold_note[x]==hold_note[x+1]):
#         # hold_note.pop(x)
#     if (hold_note[x] == hold_note[x+1]) :
#         hold_note[x] = "lol"
# H = hold_note.copy()
# for i in H:

#     if i == "lol":
#         del hold_note[hold_note.index(i)]

# # print(hold_note)
# print(c - len(hold_note))

print(c)