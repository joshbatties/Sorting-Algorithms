import random
import time

# Problem 7: Randomized Quicksort Algorithm
def randomized_quicksort(arr):
    """Performs Quicksort using a randomly selected pivot."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    pivot_count = arr.count(pivot)  # Counting pivot for duplicate values
    return randomized_quicksort(left) + [pivot] * pivot_count + randomized_quicksort(right)

# Problem 8: Quickselect with Random Pivot Choice
def quickselect(arr, k):
    """Finds the k-th smallest element in arr using Quickselect with random pivot."""
    if len(arr) <= 1:
        return arr[0]
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    pivot_count = arr.count(pivot)

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + pivot_count:
        return pivot
    else:
        return quickselect(right, k - len(left) - pivot_count)

def quicksort_with_median_pivot(arr):
    """Modifies Quicksort to use Quickselect for selecting the median as the pivot."""
    if len(arr) <= 1:
        return arr
    median_index = len(arr) // 2
    pivot = quickselect(arr, median_index)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    pivot_count = arr.count(pivot)
    return quicksort_with_median_pivot(left) + [pivot] * pivot_count + quicksort_with_median_pivot(right)

# Problem 9: Performance Comparison
def compare_quicksort_versions(n=1000):
    """Compares the performance of randomized Quicksort and Quicksort using Quickselect for median pivot."""
    test_arr = [random.randint(0, 10000) for _ in range(n)]
    
    start_time = time.time()
    randomized_quicksort(test_arr.copy())
    time_randomized_qs = time.time() - start_time

    start_time = time.time()
    quicksort_with_median_pivot(test_arr.copy())
    time_qs_median = time.time() - start_time

    return time_randomized_qs, time_qs_median

# Running the comparison
time_randomized_qs, time_qs_median = compare_quicksort_versions()
print(f"Randomized Quicksort Time: {time_randomized_qs} seconds")
print(f"Quicksort with Median Pivot Time: {time_qs_median} seconds")

#