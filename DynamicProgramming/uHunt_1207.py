import sys

def operation(r,seq1, c,seq2):

    dp = [ [0] * (c+1) for _ in range(r + 1)]

    for i in range(r+1):
        dp[i][0] = i
    for j in range(c+1):
        dp[0][j] = j

    for i in range(1,r+1):
        for j in range(1,c+1):
            if seq1[i-1] == seq2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+ min( dp[i-1][j],
                                   dp[i][j - 1],
                                   dp[i - 1][j - 1],
                                )
    return dp[r][c]


for line in sys.stdin:
    m_s,x = line.split()
    m = int(m_s)

    n_s,y = sys.stdin.readline().split()
    n = int(n_s)

    if m >= n:
        res = operation(m,x,n,y)
    else:
        res = operation(n,y,m,x)

    print(res)