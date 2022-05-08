class WeightedUF:
    '''my implementation of the weighted quick union algorithm WITH PATH COMPRESSION'''
    def __init__(self, n):
        self._uf = [i for i in range(n)]
        self._size = [1 for _ in range(n)]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def _root(self, p):
        '''finds the root of the item p'''
        root = self._uf[p]
        while root != self._uf[root]:
            self._uf[root] = self._uf[self._uf[root]]
            root = self._uf[root]

        self._uf[p] = root  
        return root

    def find(self, p):
        return self._root(p)
        

    def union(self, p, q):
        '''merges the trees of p and q'''
        p_root, q_root = self._root(p), self._root(q)

        if p_root == q_root:
            return
        
        if self._size[p_root] < self._size[q_root]:
            self._uf[p_root] = q_root
            self._size[q_root] += self._size[p_root]
        else: 
            self._uf[q_root] = p_root
            self._size[p_root] += self._size[q_root]


def main():
    uf = WeightedUF(10)
    uf.union(1, 2)
    uf.union(3, 4)
    print(uf.connected(1, 2))
    print(uf.connected(1, 5))

if __name__ == '__main__':
    main()