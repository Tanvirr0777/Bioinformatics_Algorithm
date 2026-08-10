import sys

def win_g(w,g):

    t1 = set(w)
    t2 = set()
    t3 = set()

    wrong = 0

    for char in g:
        if char in t2 or char in t3:
            continue

        if char in w:
            t2.add(char)
            if len(t1) == len(t2):
                print("You win.")
                return
        else:
            t3.add(char)
            wrong += 1
            if wrong == 7:
             print("You lose.")
             return

    print("You chickened out.")


while True:
    r = int(sys.stdin.readline())

    if r == -1:
        break

    word = sys.stdin.readline().strip()
    guss = sys.stdin.readline().strip()

    print(f"Round {r}")
    win_g(word,guss)




