import countingSort from './countingSort.js';

function radixSort(arr) {
    // Find the maximum element to determine the number of digits.
    let max_element = Math.max(...arr);

    // Initialize the digit place (e.g., 1 for units, 10 for tens, etc.).
    let place = 1;

    // Loop until we have sorted by each digit place of the maximum element.
    while (Math.floor(max_element / place) > 0) {
        // Perform counting sort on the array for the current digit place.
        // Note: The countingSort function must be able to handle sorting by digit place.
        countingSort(arr, place);

        // Move to the next digit place (e.g., from units to tens, then hundreds, etc.).
        place *= 10;
    }

    // Return the sorted array after all digit places have been processed.
    return arr;
}
// Testing the radixSort function.
console.log(radixSort([4, 2222, 0, 8, 3, 3]))
