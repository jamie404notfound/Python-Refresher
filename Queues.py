from collections import deque

def run_queues():
    queue = deque()
    queue.append(1)
    queue.append(2)
    print(queue)

    queue.popleft()
    print(queue)
    queue.appendleft(1)
    print(queue)


if __name__ == '__main__':
    run_queues()
