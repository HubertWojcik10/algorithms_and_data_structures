class InsertionSort:
    '''My own implementation of selection sort (using a class)'''
    def __init__(self, arr):
        self._arr = arr

    def sort(self):
        for i in range(1, len(self._arr)):
            curr = self._arr[i]
            j = i - 1
            while j >= 0 and curr < self._arr[j]:
                print(f'j: {j}')
                self._arr[j + 1] = self._arr[j]
                j -= 1
            self._arr[j + 1] = curr

    def show(self):
        print(self._arr)

if __name__ == '__main__':
    insertion_sort = InsertionSort([4, 7, 6, 1, 1])
    insertion_sort.sort()
    insertion_sort.show()
