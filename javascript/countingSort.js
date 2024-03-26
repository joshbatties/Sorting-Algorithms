function countingSort(arr, place = null) {
    let max_val;

    // Determine the range of the elements based on the sorting phase.
    if (place === null) {
        // If place is null, we're not sorting based on digits, so find the max of the array.
        max_val = Math.max(...arr);
    } else {
        // If sorting by digit place, set the range to be 0 to 9 (for decimal digits).
        max_val = 9;
    }

    // Create the count array.
    let count_arr = new Array(max_val + 1).fill(0); // Initialize count array with zeros.

    // Populate the count array with frequencies of each element or digit.
    if (place === null) {
        for (let num of arr) {
            count_arr[num] += 1; // Increment count for each element.
        }
    } else {
        for (let num of arr) {
            let digit = Math.floor(num / place) % 10; // Extract the relevant digit.
            count_arr[digit] += 1; // Increment count for the digit.
        }
    }

    // Transform the count array to make it cumulative.
    for (let i = 1; i < count_arr.length; i++) {
        count_arr[i] += count_arr[i - 1];
    }

    // Build the output array using the count array for positioning elements.
    let output_arr = new Array(arr.length).fill(0);
    if (place === null) {
        for (let i = arr.length - 1; i >= 0; i--) {
            let num = arr[i];
            count_arr[num] -= 1;
            let new_position = count_arr[num];
            output_arr[new_position] = num;
        }
    } else {
        for (let i = arr.length - 1; i >= 0; i--) {
            let num = arr[i];
            let digit = Math.floor(num / place) % 10;
            count_arr[digit] -= 1;
            let new_position = count_arr[digit];
            output_arr[new_position] = num;
        }
    }

    // If sorting by a specific digit, update the original array.
    if (place !== null) {
        for (let i = 0; i < arr.length; i++) {
            arr[i] = output_arr[i];
        }
    }

    // Return the sorted array. If sorting by digits, the original array is modified and returned.
    return place === null ? output_arr : arr;
}

// Test the countingSort function. (uncomment to test)
//console.log(radixSort([4, 2222, 0, 8, 3, 3]))

// Export the countingSort function for use in radixSort.
module.exports = countingSort; 