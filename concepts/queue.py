class Queue:
    '''my own implementation of the queue data structure (based on dynamic array and resizing)'''
    def __init__(self):
        self._queue = [None]
        self.n, self._front, self._back = 0, 0, 0

    def dequeue(self):
        if len(self._queue) == 0:
            raise IndexError('Queue is empty')

        dequeued = self._queue[self._front]
        self._queue[self._front] = None
        self.n -= 1
        self._front += 1

        if self._front == len(self._queue):
            self._front = 0

        if self.n < len(self._queue) // 4:
            self._resize(len(self._queue) // 2)

        return dequeued

    def enqueue(self, value):
        self._queue[self.n] = value
        self.n += 1
        self._back += 1

        if len(self._queue) == self.n:
            self._resize(2 * self.n)

    def _resize(self, capacity):
        tmp = [None] * capacity

        for i in range(self.n):
            tmp[i] = self._queue[(i + self._front) % len(self._queue)]

        self._queue = tmp
        self._front = 0
        self._back = self.n

    def peek(self):
        '''returns the recently added element to the queue'''
        return self._queue[self._front]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print(queue.peek())
