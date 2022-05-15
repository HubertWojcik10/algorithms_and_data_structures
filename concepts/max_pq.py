class MaxPQ:
    '''My own implementation of the max priority queue - the code is the same as in the min priority queue 
    with minor change when dealing with the _less function'''
    def __init__(self):
        self._pq = [None] #the first index will be empty
        self._n = 0

    def is_empty(self):
        return self._n == 0

    def show(self):
        return self._pq[1:]
    
    def insert(self, x):
        self._pq.append(x)
        self._n += 1

        #bottom-up violation of the heap order, that's why we need to swim
        self._swim(self._n)

    def del_max(self):
        #exchange the first and last element before sinking
        self._exch(1, self._n)
        maxim = self._pq.pop()
        self._n -= 1

        #top-down violation of the heap order, that's why we need to sink
        self._sink(1)

        return maxim
    
    def _swim(self, k):
        while k > 1 and self._less(k // 2, k):
            self._exch(k // 2, k)
            k = k // 2
    
    def _sink(self, k):
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._less(j, j+1):
                j += 1
            if not self._less(k, j):
                break

            self._exch(k, j)

            k = j
        
    def _less(self, i, j):
        return self._pq[i] < self._pq[j]

    def _exch(self, i, j):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    def __len__(self):
        return str(self._n)


if __name__ == '__main__':
    maxpq = MaxPQ()
    maxpq.insert(5)
    maxpq.insert(3)
    maxpq.insert(7)
    maxpq.insert(2)
    maxpq.del_max()

    maxpq.del_max()
    maxpq.insert(20)
    maxpq.insert(1)

    print(maxpq.show())


    
