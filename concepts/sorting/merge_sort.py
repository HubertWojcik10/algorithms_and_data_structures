def merge_sort(arr):
    '''
    A recursive implementation of merge sort algorithm (linearithmic time)
    '''
    length = len(arr)
    
    if length == 1: return arr

    arr1 = merge_sort(arr[:length//2])
    arr2 = merge_sort(arr[length//2:])

    return merge(arr1, arr2)

def merge(arr1, arr2):
    '''
    A helper function that merges two sorted arrays in linear time
    '''
    i, j, k = 0, 0, 0
    new_arr = (len(arr1) + len(arr2))*[0]

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]: 
            new_arr[k] = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            new_arr[k] = arr2[j]
            j += 1
        elif arr1[i] == arr2[j]: 
            new_arr[k] = arr1[j]
            new_arr[k+1] = arr2[j]
            i += 1
            j += 1
            k += 1

        k += 1
    
    # the values remaining (possibly) in the arr1
    while i < len(arr1):
        new_arr[k] = arr2[i]
        k += 1
        i += 1

    # the values remaining (possibly) in the arr2
    while j < len(arr2):
        new_arr[k] = arr2[j]
        k += 1
        j += 1

    return new_arr

arr1 = [1, 2, 7, 3, 4, 4, 2, 8]
arr2 = [5, 6, 7, 8]
print(merge_sort(arr1))