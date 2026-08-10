import sys

def top_index(temp):
    mx = max(temp)
    index = []

    for k in range(len(temp)):
      if temp[k] == mx:
          index.append(k)
    return index


def print_out(st,ind):
    for j in ind:
        print(st[j])


t = int(sys.stdin.readline())

for i in range(t):
    count = 0
    web = []
    prio = []
    while count < 10:
        line = sys.stdin.readline().strip()

        if not line:
            continue

        site, value = line.split()
        value = int(value)
        web.append(site)
        prio.append(value)

        count += 1

    print(f"Case #{i+1}:")
    print_out(web,top_index(prio))


#--------------------------#more efficient way-------
"""

import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    mx = -1
    ans = []

    for _ in range(10):
        line = sys.stdin.readline().strip()

        if not line:
            continue

        site, value = line.split()
        value = int(value)

        if value > mx:
            mx = value
            ans = [site]
        elif value == mx:
            ans.append(site)

    print(f"Case #{case}:")
    for site in ans:
        print(site)

"""