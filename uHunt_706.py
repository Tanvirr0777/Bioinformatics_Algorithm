import sys

segments = {
    '0': [1, 1, 1, 0, 1, 1, 1],
    '1': [0, 0, 1, 0, 0, 1, 0],
    '2': [1, 0, 1, 1, 1, 0, 1],
    '3': [1, 0, 1, 1, 0, 1, 1],
    '4': [0, 1, 1, 1, 0, 1, 0],
    '5': [1, 1, 0, 1, 0, 1, 1],
    '6': [1, 1, 0, 1, 1, 1, 1],
    '7': [1, 0, 1, 0, 0, 1, 0],
    '8': [1, 1, 1, 1, 1, 1, 1],
    '9': [1, 1, 1, 1, 0, 1, 1]
}

for line in sys.stdin:
    s, n = line.split()

    if s == '0' and n == '0':
        break

    s = int(s)
    rows = 2 * s + 3

    for r in range(rows):
        parts = []

        for d in n:
            seg = segments[d]

            if r == 0:
                parts.append(
                    " " + ("-" * s if seg[0] else " " * s) + " "
                )

            elif 1 <= r <= s:
                parts.append(
                    ("|" if seg[1] else " ")
                    + (" " * s)
                    + ("|" if seg[2] else " ")
                )

            elif r == s + 1:
                parts.append(
                    " " + ("-" * s if seg[3] else " " * s) + " "
                )

            elif s + 2 <= r <= 2 * s + 1:
                parts.append(
                    ("|" if seg[4] else " ")
                    + (" " * s)
                    + ("|" if seg[5] else " ")
                )

            else:
                parts.append(
                    " " + ("-" * s if seg[6] else " " * s) + " "
                )

        print(" ".join(parts))

    print()

