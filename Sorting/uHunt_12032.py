import sys

t = int(sys.stdin.readline())

for j in range(t):
    n = int(sys.stdin.readline())

    steps_temp = list(map(int, sys.stdin.readline().split()))
    steps = steps_temp[:n]

    diff = [steps[0]]

    for s in range(1,n):
        diff.append(steps[s] - steps[s-1])

    k = max(diff)
    
    while True:
        k_s = k
        temp = 1

        for jump in diff:
            if jump > k_s:
                temp = 0
                break

            if jump == k_s:
                k_s -= 1

        if temp == 1:
            break

        k += 1

    print(f"Case {j + 1}: {k}")