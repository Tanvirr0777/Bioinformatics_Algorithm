import sys

def location(direction,ori):
    if direction.upper() == "LEFT":
        ori -= 1
    if direction.upper() == "RIGHT":
        ori += 1
    return ori


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    ins = []
    insNum = 0
    origin = 0
    while n > 0:
        instruction = sys.stdin.readline().split()

        if len(instruction) > 1:
            insNum = int(instruction[2])
            temp = ins[insNum-1]
            ins.append(temp)

        else:
            ins.append(instruction[0])

        if len(instruction) > 1:
            insNum -= 1
            origin = location(ins[insNum],origin)
        else:
            origin = location(instruction[0],origin)

        n -= 1
    print(origin)
