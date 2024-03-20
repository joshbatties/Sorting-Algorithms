def counting_sort(arr, place=None):
    # Determine the range of the elements based on the sorting phase.
    if place is None:
        # If place is None, we're not sorting based on digits, so find the min and max of the array.
        min_val = min(arr)
        max_val = max(arr)
    else:
        # If sorting by digit place, set the range to be 0 to 9 (for decimal digits).
        min_val = 0  
        max_val = 9  

    # Calculate the range of elements to create the count array.
    range_of_elements = max_val - min_val + 1
    count_arr = [0] * range_of_elements  # Initialize count array with zeros.

    # Populate the count array with frequencies of each element or digit.
    if place is None:
        for num in arr:
            count_arr[num - min_val] += 1  # Increment count for each element.
    else:
        for num in arr:
            digit = (num // place) % 10  # Extract the relevant digit.
            count_arr[digit - min_val] += 1  # Increment count for the digit.

    # Transform the count array to make it cumulative.
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Build the output array using the count array for positioning elements.
    output_arr = [0] * len(arr)
    if place is None:
        for num in reversed(arr):
            # Place each element in the correct position in the output array.
            count_arr[num - min_val] -= 1
            new_position = count_arr[num - min_val]
            output_arr[new_position] = num
    else:
        for num in reversed(arr):
            # Place each digit in the correct position in the output array.
            digit = (num // place) % 10
            count_arr[digit - min_val] -= 1
            new_position = count_arr[digit - min_val]
            output_arr[new_position] = num

    # If sorting by a specific digit, update the original array.
    if place is not None:
        for i in range(len(arr)):
            arr[i] = output_arr[i]

    # Return the sorted array. If sorting by digits, the original array is modified and returned.
    return output_arr if place is None else arr


if __name__ == "__main__":
    print(counting_sort([4, 2, 2, 8, 3, 0, 3, 1, 96]))
