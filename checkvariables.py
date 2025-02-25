def check():
    n = 1
    x, y, z = 0.135, "abc", False
    # n = n + 1
    # n += 1
    for i in range(3):
        if i < 3:
            n += 1
            if n != 1 and n == 3:
                print("n = ", 3)

    for i in range(5, 0, -1):
        print(i)

    z = None
    print("z = ", z)

    # Decimal Division is default
    print(5 / 2)
    # Two Slashes Rounds Down Integer
    print(5 // 2)

    print(int(-3 / 2))
    print(int(-10 % 3))
    import math
    print(math.fmod(-10, 3))

if __name__ == '__main__':
    check()