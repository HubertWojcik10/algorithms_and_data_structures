class MergeSort():
    '''My own implementation of merge sort (based on divide and conquer method)'''
    def __init__(self, array):
        self._arr = array
        self.n = len(array)

    def sort(self):
        tmp = [None] * self.n
        self._merge_sort(self._arr, tmp, 0, self.n-1)
    
    def _merge_sort(self, arr, tmp, l, h):
        if h <= l:
            return
        mid = l + (h - l) // 2

        self._merge_sort(arr, tmp, l, mid)
        self._merge_sort(arr, tmp, mid+1, h)

        self._merge(arr, tmp, l, mid, h)
        
    def _merge(self, arr, tmp, l, m, h):
        i, j = l, m+1

        for k in range(l, h+1):
            tmp[k] = arr[k]

        for k in range(l, h+1):
            if i > m:
                arr[k] = tmp[j]
                j += 1
            elif j > h:
                arr[k] = tmp[i]
                i += 1
            elif tmp[j] < tmp[i]:
                arr[k] = tmp[j]
                j += 1
            else:
                arr[k] = tmp[i]
                i += 1

        return arr   

    def show(self):
        print(self._arr)


if __name__ == '__main__':
    merge_sort = MergeSort([4, 7, 6, 1, 1, 4, 10, 12, 2])
    merge_sort.sort()
    merge_sort.show()