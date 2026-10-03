import re
import sys

def match(seq1,seq2):
    m = len(seq1)
    n = len(seq2)

    dp =[[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq2[i-1] == seq1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]

case = 1
for line in sys.stdin:

    seq1_t = line
    seq2_t = sys.stdin.readline()

    seq1_s = re.sub(r"[^a-zA-z\s]"," ",seq1_t)
    seq2_s = re.sub(r"[^a-zA-z\s]"," ",seq2_t)

    seq1 = seq1_s.split()
    seq2 = seq2_s.split()


    if len(seq1) == 0 or len(seq2) == 0:
        print(f"{case:2}. Blank!")
    else:
        res = match(seq1,seq2)
        print(f"{case:2}. Length of longest match: {res}")

    case += 1