
class UF:
    ''' my implementation of the quick find algorithm '''
    def __init__(self, n):
        self._id = [i for i in range(n)] # initialize the array

    def connected(self, p, q):
        return self._id[p] == self._id[q]
    
    def union(self, p, q):
        p_id, q_id = self._id[p], self._id[q]

        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id # all elements whose id is p_id will have now id q_id
        

def main():
    uf = UF(10)
    uf.union(1, 2)
    uf.union(3, 4)
    print(uf.connected(1, 2))
    print(uf.connected(1, 5))


if __name__ == '__main__':
    main()
