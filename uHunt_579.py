import sys

f = sys.stdin

for line in f:
    h,m = line.split(":")

    h = int(h)
    m = int(m)
    if h == 0 and m == 00:
        break

    m_pos = m*6
    h_pos = (h*30) + (m*0.5)

    no_ang = abs(h_pos - m_pos)
    ang = min((360-no_ang), no_ang)
    print(f"{ang:.3f}")

