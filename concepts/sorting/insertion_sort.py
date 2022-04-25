'''
implementation of insertion sort algorithm
'''
def insertion_sort(arr):
    for i in range(len(arr)-1):
        j = i
        while arr[j+1] < arr[j] and j >= 0:
            curr = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = curr
            j -= 1

    return arr

#print(insertion_sort([8, 5, 3, 7, 9]))
print(insertion_sort(['D', 'G', 'H', 'A', 'B']))
        
