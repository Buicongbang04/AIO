from queue import Queue

queue1 = Queue(5)

queue1.enqueue(1)

queue1.enqueue(2)

print('Queue 1 is full: ', end='')
print(queue1.is_full())

print('The front of queue 1 now is: ', end='')
print(queue1.front())

print('Queue 1 dequeue is: ', end='')
print(queue1.dequeue())

print('The front of queue 1 now is: ', end='')
print(queue1.front())

print('Queue 1 dequeue is: ', end='')
print(queue1.dequeue())

print('Queue 1 is empty: ', end='')
print(queue1.is_empty())