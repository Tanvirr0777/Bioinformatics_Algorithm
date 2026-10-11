import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

incoming = []
outgoing = []

for _ in range(m):

    d, f, t, c = map(int, input().split())

    if t == 0:
        incoming.append((d, f, c))
    else:
        outgoing.append((d, t, c))

incoming.sort()
outgoing.sort()


INF = 10**30

best = [INF] * (n + 1)
total = 0
count = 0

arrivals = []

i = 0

while i < len(incoming):

    day = incoming[i][0]

    while i < len(incoming) and incoming[i][0] == day:

        day, city, cost = incoming[i]

        if cost < best[city]:

            if best[city] == INF:
                count += 1
            else:
                total -= best[city]

            best[city] = cost
            total += cost

        i += 1

    if count == n:
        arrivals.append((day, total))


best = [INF] * (n + 1)
total = 0
count = 0

departures = []

i = len(outgoing) - 1

while i >= 0:

    day = outgoing[i][0]

    while i >= 0 and outgoing[i][0] == day:

        day, city, cost = outgoing[i]

        if cost < best[city]:

            if best[city] == INF:
                count += 1
            else:
                total -= best[city]

            best[city] = cost
            total += cost

        i -= 1

    if count == n:
        departures.append((day, total))

departures.reverse()



res = INF

for arrival_day, arrival_cost in arrivals:

    req_departure = arrival_day + k + 1

    left = 0
    right = len(departures) - 1

    while left <= right:

        mid = (left + right) // 2

        if departures[mid][0] >= req_departure:
            right = mid - 1
        else:
            left = mid + 1

    if left < len(departures):

        departure_day, departure_cost = departures[left]

        res = min( res,arrival_cost + departure_cost)


if res == INF:
    print(-1)
else:
    print(res)