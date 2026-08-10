
import sys

f = sys.stdin

i = 1
for line in f:
    l = line.strip().upper()

    if l == "#":
        break
    elif l == "HELLO":
        print(f"Case {i}: ENGLISH")
    elif l == "HOLA":
        print(f"Case {i}: SPANISH")
    elif l == "HALLO":
        print(f"Case {i}: GERMAN")
    elif l == "BONJOUR":
        print(f"Case {i}: FRENCH")
    elif l == "CIAO":
        print(f"Case {i}: ITALIAN")
    elif l == "ZDRAVSTVUJTE":
        print(f"Case {i}: RUSSIAN")
    else:
        print(f"Case {i}: UNKNOWN")
    i += 1



