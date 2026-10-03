import sys

f = sys.stdin

for line1 in f:

    line1 = line1.strip()

    if line1 == "":
        continue

    n = int(line1)

    line2 = next(f).strip()
    num = line2.split()
    num_int = list(map(int, num))

    line3 = next(f).strip()
    cost = int(line3)

    num_list = sorted(num_int)

    low = 0
    high = len(num_list) - 1

    c1,c2 = 0,0
    while low < high :
        s = num_list[low] + num_list[high]
        if s > cost:
            high -= 1
        elif s == cost :
            c1 = num_list[low]
            c2 = num_list[high]
            low +=1
            high -= 1
        else:
            low +=1
    print(f"Peter should buy books whose prices are {c1} and {c2}.")
    print()

