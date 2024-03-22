from python.counting_sort import counting_sort

def radix_sort(arr):
    # Find the maximum element to determine the number of digits.
    max_element = max(arr)

    # Initialize the digit place (e.g., 1 for units, 10 for tens, etc.).
    place = 1

    # Loop until we have sorted by each digit place of the maximum element.
    while max_element // place > 0:
        # Perform counting sort on the array for the current digit place.
        # Note: The counting_sort function must be able to handle sorting by digit place.
        counting_sort(arr, place)

        # Move to the next digit place (e.g., from units to tens, then hundreds, etc.).
        place *= 10

    # Return the sorted array after all digit places have been processed.
    return arr


if __name__ == "__main__":
    print(radix_sort([121, 12, 132, 51, 4011, 222, 61, 99, 0]))