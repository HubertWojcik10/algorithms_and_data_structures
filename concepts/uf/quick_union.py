class UF:
    '''my implementation of the quick union algorithm'''
    def __init__(self, n):
        self._uf = [i for i in range(n)]
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def find(self, p):
        '''finds the root of the item p'''
        while self._uf[p] != p:
            # we go up the tree until we find an item that has its root as itself (the root of the tree)
            p = self._uf[p] 
        
        return p

    def union(self, p, q):
        '''merges the trees of p and q'''
        p_root, q_root = self.find(p), self.find(q)

        if p_root == q_root:
            return
        
        self._uf[q_root] = p_root


def main():
    uf = UF(10)
    uf.union(1, 2)
    uf.union(3, 4)
    print(uf.connected(1, 2))
    print(uf.connected(1, 5))

if __name__ == '__main__':
    main()