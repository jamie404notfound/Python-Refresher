# Arrays are called lists in Python

def run_arrays():
    arr = [1, 2, 3]
    print(arr)
    # Can be used as a Stack
    arr.append(4)
    arr.append(5)
    print(arr)
    arr.pop()
    print(arr)
    arr.insert(1, 7)
    print(arr)
    arr[0] = 0
    arr[3] = 0
    print(arr)

    n = 5
    arr2 = [1] * n
    print(arr2)

    # Array loop
    nums = [4, 5, 6]

    # Using Index
    for i in range(len(nums)):
        print(nums[i])

    # Without Index
    for n in nums:
        print(n)

    # With index and value
    for i, n in enumerate(nums):
        print(f'Index: {i}\tValue: {n}')

    # Loop multiple arrays simultaneously with unpacking
    nums2 = [1, 2, 3]
    nums3 = [4, 5, 6]

    for n1, n2 in zip(nums2, nums3):
        print(f'{n1}\t{n2}')

    nums2.reverse()
    print(nums2)
    # nums2.sort(reverse=True)
    nums2.sort()
    print(nums2)

    arr3 = ["bob", "alice", "jane", "doe"]
    arr3.sort()
    print(arr3)

    # Custom sort (by length of string)
    arr3.sort(key=lambda x: len(x))
    print(arr3)

    # List Comprehension
    arr4 = [i+i for i in range(5)]
    print(arr4)

if __name__ == '__main__':
    run_arrays()
