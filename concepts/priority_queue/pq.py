'''
My implementation of the MAX priority queue algorithm.
'''
class MPQ:
    def __init__(self, _max: int = 1, test=False):
        self._pq = [None] * (_max + 1)
        self._n = 0
        self._test = test

    def insert(self, item):
        #check if there is size in _pq array to insert the item 
        if self._n == len(self._pq) - 1:
            self._resize(1*len(self._pq))
        
        #insert the item
        self._n += 1
        self._pq[self._n] = item

        #order the array to maintain the heap structure
        self._swim(self._n)
        if self._test: 
            print(f'inserted{item}')
            print(f'queue: {self._pq}')

    def max(self):
        assert self._pq[1] #in other case, raise and Assertion Error
        return self._pq[1]

    def del_max(self):
        _max = self._pq[1]
        assert _max is not None

        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        self._pq[self._n + 1] = None

        #resize if there is too much free space in the queue
        if self._n > 0 and self._n == (len(self._pq) - 1) // 4:
            self._resize(len(self._pq) // 2)

        return _max

    def _swim(self, k:int):
        #move the item from index k up
        while k > 1 and self._less(k // 2, k):
            if self._test: print(f'Changing {self._pq[k]} with {self._pq[k//2]}')
            self._exch(k, k // 2)
            k = k // 2

    def _sink(self, k:int):
        #move the item from index k down
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._less(j, j + 1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def _resize(self, capacity):
        temp = self._pq
        temp += [None] * capacity

        return temp
    
    def _less(self, i:int, j:int):
        return self._pq[i] < self._pq[j]

    def _exch(self, i: int, j: int):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    

def main():
    #mpq = MPQ(test=True)
    #mpq.insert(9)
    #mpq.insert(10)
    #mpq.insert(11)
    #print(mpq.del_max())
    #mpq.insert(1)
    #mpq.insert(3)
    #mpq.insert(32)
    #print(mpq.del_max())
    pass

if __name__ == '__main__':
    main()