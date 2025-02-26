# HashMap (aka dict)

def hash_map():
    my_map = {}
    print(my_map)
    my_map["alice"] = 88
    my_map["bob"] = 77
    print(my_map)
    print(len(my_map))
    my_map["alice"] = 80
    print(my_map)

    print("alice" in my_map)
    my_map.pop("alice")
    print("alice" in my_map)

    # Dict Comprehension
    my_map = {i: 2 * i for i in range(3)}
    print(my_map)

    # Looping through maps
    my_map = {"alice": 90, "bob": 70}
    for key in my_map:
        print(key,my_map[key])

    for val in my_map.values():
        print(val)

    for key,val in my_map.items():
        print(key," : ", val)


if __name__ == '__main__':
    hash_map()
