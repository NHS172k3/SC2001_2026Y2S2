def partition(low, high, array, comparisons):
    pivot = (low+high)//2
    array = swap(pivot, low, array)
    last_small = low
    element = low + 1
    while element <= high:
        # recall that we swapped pivot and low, so we need to access array[low]
        comparisons += 1
        if array[element] < array[low]:
            array = swap(element, last_small+1, array)
            last_small += 1
        # We can do this because everything between element and last_small has ideally already been searched and settled. so we can always increment
        element += 1


    
    # Now we need to putback the element into the position of last_small
    array = swap(low, last_small, array)
    return last_small, comparisons

def swap(first, second, array):
    array[first], array[second] = array[second], array[first]
    return array

def quicksort(low, high, array, comparisons):
    if low >= high:
        return array, comparisons
    pivot, comparisons = partition(low, high, array, comparisons)
    array, comparisons = quicksort(low, pivot-1, array, comparisons)
    array, comparisons = quicksort(pivot+1, high, array, comparisons)
    return array, comparisons

print(quicksort(0, 7,[1,-14,2,3,4,5,6,8], 0))