class SelectionSort:
    '''My own implementation of selection sort using a class'''
    def __init__(self, array):
        self._arr = array
        self.n = len(array)

    def sort(self):
        for i in range(self.n):
            min_index = i
            for j in range(i+1, self.n):
                if self._arr[j] < self._arr[min_index]:
                    min_index = j
            self._arr[i], self._arr[min_index] = self._arr[min_index], self._arr[i]
        return self._arr


if __name__ == '__main__':
    selection_sort = SelectionSort([4, 7, 6, 1, 1])
    print(selection_sort.sort())