def my_func(n, m):
    return n * m


# Nest functions have access to outer variables
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()


# Can modify objects but not reassign unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying the array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # Will only modify val in the helper scope
        # val *= 2
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)

if __name__ == '__main__':
    print(my_func(3, 4))
    print(outer('a', 'b'))
