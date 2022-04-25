'''
My own implementation of the selection sort (not optimized) algorithm for both strings and lists of integers.
selection_sort() is the main function, _find_min() helps with finding the minimum value of the rest of the list.
'''
def selection_sort(arr, num=False):
    for i in range(len(arr)):
        minimum, i_of_min = _find_min(arr[i+1:],  i+1, num)
        if arr[i] > minimum: 
            arr[i_of_min] = arr[i]
            arr[i] = minimum

    return arr

def _find_min(arr, x, num):
    if num: min = 999999
    else: min = 'Z'
    i_of_min = 0
    for i in range(len(arr)):
        if arr[i] < min: 
            min = arr[i]
            i_of_min = i + x
    return min, i_of_min   

print(selection_sort([3, 5, 6, 1, 2], num=True))
print(selection_sort(list('EASYQUESTION')))
