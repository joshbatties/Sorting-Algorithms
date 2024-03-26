def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1  # Initialize 'right' on the first call

    # Base condition: if the part of the array has only one element or is invalid
    if left >= right:
        return arr

    # Partition the array around a pivot and get the index of the pivot element
    pivot_index = partition(arr, left, right)

    # Recursively sort the parts of the array before and after the partition
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)

    # Return the sorted array
    return arr

def partition(arr, left, right):
    # The rightmost element is chosen as the pivot
    pivot_value = arr[right]
    # The 'partition_index' will track the final position of the pivot
    partition_index = left

    for i in range(left, right):
        # If an element is smaller than the pivot, it is moved to the 'left' part
        if arr[i] < pivot_value:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]  # Swap elements
            partition_index += 1  # Move the partition index to the right

    # Place the pivot at its final place (all elements left to it are smaller)
    arr[partition_index], arr[right] = arr[right], arr[partition_index]
    return partition_index  # Return the final position of the pivot


# Testing
if __name__ == "__main__":
    print(quick_sort([-1, -400, 121, 12, 132, 51, 61, 99]))  