import sys

tc = int(sys.stdin.readline())

for it in range(0,tc):

    line = sys.stdin.readline().strip()

    while line == "":
        line = sys.stdin.readline().strip()

    n = int(line)

    people = []
    for i in range(n):
        a = int(sys.stdin.readline())
        people.append(a)

    people.sort()

    total = 0
    ans = []

    while n > 3:

        a = people[0]
        b = people[1]
        y = people[n - 2]
        z = people[n - 1]

        cost1 = a + 2 * b + z
        cost2 = 2 * a + y + z

        if cost1 <= cost2:

            total += cost1

            ans.append((a,b))
            ans.append((a,))
            ans.append((y,z))
            ans.append((b,))

        else:
            total += cost2

            ans.append((a,z))
            ans.append((a,))
            ans.append((a,y))
            ans.append((a,))

        n -= 2

    if n == 3 :
        a = people[0]
        b = people[1]
        c = people[2]

        total += a+b+c

        ans.append((a,b))
        ans.append((a,))
        ans.append((a,c))

    elif n == 2:
        total += people[1]
        ans.append((people[0],people[1]))

    elif n == 1:
        total += people[0]
        ans.append((people[0],))

    print(total)
    for num in ans:
        print(*num)

    if it != tc - 1:
        print()