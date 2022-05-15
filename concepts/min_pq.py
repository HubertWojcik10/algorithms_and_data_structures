class MinPQ:
    '''My own implementation of the min priority queue'''
    def __init__(self):
        self._pq = [None] #the first index will be empty
        self._n = 0

    def is_empty(self):
        return self._n == 0

    def show(self):
        return self._pq[1:]

    def get_min(self):
        return self._pq[1]
    
    def insert(self, x):
        self._pq.append(x)
        self._n += 1

        #bottom-up violation of the heap order, that's why we need to swim
        self._swim(self._n)

    def del_min(self):
        #exchange the first and last element before sinking
        self._exch(1, self._n)
        min = self._pq.pop()
        self._n -= 1

        #top-down violation of the heap order, that's why we need to sink
        self._sink(1)

        return min
    
    def _swim(self, k):
        while k > 1 and self._less(k, k // 2):
            self._exch(k // 2, k)
            k = k // 2
    
    def _sink(self, k):
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._less(j+1, j):
                j += 1
            if not self._less(j, k):
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
    minpq = MinPQ()
    minpq.insert(5)
    minpq.insert(3)
    minpq.insert(7)
    minpq.insert(2)
    minpq.del_min()

    minpq.del_min()
    minpq.insert(20)
    minpq.insert(1)

    print(minpq.show())


    
