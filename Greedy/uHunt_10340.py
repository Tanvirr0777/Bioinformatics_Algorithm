import sys

for line in sys.stdin:
    words = line.strip().split()

    s_i = words[0]
    temp = words[1]
    t_i = ""

    for i in range(len(temp)):
        if temp[i] in s_i :
            t_i += temp[i]

    s = list(s_i)
    t = list(t_i)

    track,k = 0,0
    l = len(s)
    inter = t.copy()

    for i in range(l):

        if s[i] in inter:
            k = inter.index(s[i])
        else:
            k = -1
            break

        inter = inter[k+1:]
        track += 1

    if track == l :
        print("Yes")
    else:
        print("No")
