function mergeSort(arr) {
    // Find the middle point to divide the array into two halves
    const mid = arr.length / 2;

    // Base case: if the array has less than two elements, return it as is
    if (arr.length < 2) {
      return arr;
    }
    //Recursively sort the two halves and merge 
    const left = arr.splice(0, mid);
    return merge(mergeSort(left), mergeSort(arr));
  }
  
  function merge(left, right) {
    // Initialize an empty array to store the merged array
    let arr = [];

    // Compare the first elements of each array and append the smaller one to 'arr'
    // Repeat until one of the arrays is empty
    while (left.length && right.length) {
      if (left[0] < right[0]) {
        arr.push(left.shift());
      } else {
        arr.push(right.shift());
      }
    }
    
    // Concatenate the remaining elements from 'left' or 'right' to 'arr' (one will be empty)
    // Return the sorted array
    return [...arr, ...left, ...right];
  }

console.log(mergeSort([121, 12, 132, 51, 61, 99, 200, 0, -1]))