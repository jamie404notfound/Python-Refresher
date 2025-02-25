# Strings are similar to arrays

def strings():
    s = "abc"
    # Slice string
    print(s[0:2])

    # Strings are Immutable, this won't work
    # s[0] = "A"
    # Have to create new string
    s += "def"
    print(s)

    # Valid numeric strings can be converted
    print(int("123") + int("123"))
    # Numbers can be converted to strings
    print(str(123) + str(123))

    # ASCII value of char
    print("Ascii value of a:", ord("a"))

    # Combine list of strings
    # (with an empty string delimiter)
    strings = ["ab","cd","ef"]
    print("".join(strings))


if __name__ == '__main__':
    strings()
