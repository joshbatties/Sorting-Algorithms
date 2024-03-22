function selectionSort(arr) {
    // Traverse through all array elements
    for (let i = 0; i < arr.length; i++) { 
      // Find the minimum element in remaining unsorted array
      let min = i; 
      for (let j = i + 1; j < arr.length; j++) { 
        if (arr[j] < arr[min]) {
          min = j;   
        }
      }

      // Swap the found minimum element with the first element, if needed
      if (min !== i) {
        [arr[i], arr[min]] = [arr[min], arr[i]]; 
      }
    }
    // Return the sorted array
    return arr; 
  }

console.log(selectionSort([121, 12, 132, 51, 61, 99, 200, 0, -1]));