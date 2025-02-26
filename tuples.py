# Tuples are like arrays but immutable
def my_tuples():
    tup = (1, 2, 3)
    print(tup)
    print(tup[0])
    print(tup[-1])

    maps = {(1, 2): 3}
    print(maps)
    print(maps[(1, 2)])

    sets = set()
    sets.add((1, 2))
    print((1, 2) in sets)

    # Lists can't be keys


if __name__ == '__main__':
    my_tuples()
