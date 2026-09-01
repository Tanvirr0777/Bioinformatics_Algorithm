import sys

word_f = sys.stdin.readline().strip()
word_l = sys.stdin.readline().strip()
word_l_rev = word_l[::-1]

if word_f == word_l_rev:
    print("YES")
else:
    print("NO")