a = [[10,8],[5,6]]



'''
n = "cheese"
n = set(n)

print(n)

x = 'chese'
x = set(x)

for c in x:
    if c in n:
        print(c)







import sys

r = int(sys.stdin.readline())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

for i in range(r):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=' ')
    print()



""" 

def function(n):
    if n == 4:
        return n
    else:
        return 2 * function(n + 1)

print(function(2))

#recursive factorial

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(0))

def outer():
    def inner():
        print("You know?")

    return inner

func = outer()
func()
'''
