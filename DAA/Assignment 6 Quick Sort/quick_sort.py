import random
import timeit

def partition(array, low, high):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
  
    # Pointer for greater element
    i = low - 1
  
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
  
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    # Return the position from where partition is done
    return i + 1
  
# Function to perform quicksort
  
  
def quick_sort(array, low, high):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)

def partition_random(array, low, high):
    pivot = random.randrange(low,high)
    array[high], array[pivot] = array[pivot], array[high]
    return partition(array,low,high)

def quick_sort_random(array,low,high):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition_random(array, low, high)
  
        # Recursive call on the left of pivot
        quick_sort_random(array, low, pi - 1)
  
        # Recursive call on the right of pivot
        quick_sort_random(array, pi + 1, high)

array = [10, 7, 8, 9, 1, 5, 3, 23,45,21,66,12,55,86,12]

start = timeit.default_timer()
quick_sort(array, 0, len(array) - 1)
end = timeit.default_timer()
  
print(f'Sorted array: {array}')
print("%.10f" %(end-start))

start = timeit.default_timer()
quick_sort_random(array, 0, len(array) - 1)
end = timeit.default_timer()
  
print(f'Sorted array: {array}')
print("%.10f" % (end-start))