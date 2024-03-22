def merge_sort(arr):
    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Base case: if the array has less than two elements, return it as is
    if len(arr) < 2:
        return arr

    # Recursively sort the two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves and return
    return merge(left, right)
    
def merge(left, right):
    # Initialize an empty array to store the merged array
    arr = []

    # Compare the first elements of each array and append the smaller one to 'arr'
    # Repeat until one of the arrays is empty
    while left and right:
        if left[0] < right[0]:
            arr.append(left.pop(0))
        else:
            arr.append(right.pop(0))

    # Concatenate the remaining elements from 'left' or 'right' to 'arr' (one will be empty)
    # Return the sorted array
    return arr + left + right

if __name__ == "__main__":
    print(merge_sort([-1, -400, 121, 12, 132, 51, 61, 99]))
