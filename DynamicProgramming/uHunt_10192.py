import sys

def visitcity(s1,s2):
    m = len(s1) - 1
    n = len(s2) - 1

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


case = 1
for line in sys.stdin:
    s1 = line
    if s1.startswith('#'):
        break
    s2 = sys.stdin.readline()

    res = visitcity(s1,s2)

    print(f"Case #{case}: you can visit at most {res} cities.")
    case += 1