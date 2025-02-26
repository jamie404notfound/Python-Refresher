# Heaps under the hood are arrays
import heapq


def heaps():
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 4)
    print(minHeap)

    # Min is always at index [0]
    print(f'Minimum: {minHeap[0]}')

    while len(minHeap):
        print(heapq.heappop(minHeap))

    # No Maps heap by default, workaround
    # Use min heap and multiply by -1
    # push & pop
    maxheap = []
    heapq.heappush(maxheap, -3)
    heapq.heappush(maxheap, -2)
    heapq.heappush(maxheap, -4)
    # Max is always at index [0]
    print(-1 * maxheap[0])
    while len(maxheap):
        print(-1 * heapq.heappop(maxheap))

    # Build heap from initial values
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))


if __name__ == '__main__':
    heaps()
