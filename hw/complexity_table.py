import math

print("O(n)".center(10),"O(log2n)".center(10),"O(nlog2n)".center(10),"O(n^2)".center(10),"O(n^3)".center(10),"O(2^n)".center(12),"O(n!)".center(48))
i = 1
while i < 50:
    print(f"{str(i).center(10)} {str(math.log2(i)).center(10)} {str(i * math.log2(i)).center(10)} {str(i ** 2).center(10)}"
    f"{str(i ** 3).center(12)} {str(2 ** i).center(10)} {str(math.factorial(i) ).center(50)}")

    i = i * 2