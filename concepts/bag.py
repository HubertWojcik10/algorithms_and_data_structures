class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node

class LinkedListBag:
    '''My implementation of the bag data structure (based on a linked list)'''
    def __init__(self):
        self._first = None
        self._n = 0

    def insert(self, value):
        old_first = self._first
        self._first = Node(value, old_first)
        self._n += 1

    def __len__(self):
        '''enables us to use len() method on the bag'''
        return self._n
    
    def __iter__(self):
        '''makes the bag iterable'''
        first = self._first
        while first != None:
            yield first.item
            first = first.next


if __name__ == '__main__':
    bag = LinkedListBag()
    bag.insert(3)
    bag.insert(2)
    bag.insert(4)
    for item in bag:
        print(item)

    print(f'length of the bag: {len(bag)}')