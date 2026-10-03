import sys

def longestsubseq(seqm, seqt):
    lm = len(seqm)
    lt = len(seqt)

    dp = [[0]*(lm+1) for _ in range(lt + 1)]

    for i in range(1, lt + 1):
        for j in range(1, lm + 1):
            if seqt[i-1] == seqm[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[lt][lm]


for line in sys.stdin:
    seqm = line.strip()
    seqt = sys.stdin.readline().strip()

    res = longestsubseq(seqm, seqt)
    print(res)
