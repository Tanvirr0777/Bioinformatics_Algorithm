import sys

t = int(sys.stdin.readline())


for i in range(t):

    marks_arr_temp = list(map(int, sys.stdin.readline().split()))
    marks_arr = marks_arr_temp[:7]

    without_class_test = sum(marks_arr[:4])

    class_test = marks_arr[4:]
    c = sorted(class_test)

    c_mark = (c[1]+c[2]) / 2

    x = without_class_test + c_mark


    if x >= 90:
        print(f"Case {i + 1}: A")
    elif x >= 80:
        print(f"Case {i + 1}: B")
    elif x >= 70:
        print(f"Case {i + 1}: C")
    elif x >= 60:
        print(f"Case {i + 1}: D")
    else:
        print(f"Case {i + 1}: F")


