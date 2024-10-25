// let a = [1, 6, 3, 7, 1, 3, 5, 1, 3];
// let arr = [];    // This will keep track of elements we have seen
// let arr1 = [];   // This will keep track of duplicates

// // Iterate over each element in the array a
// for (let i = 0; i < a.length; i++) {
//     // If the element has already been seen and is not already in arr1, add it to arr1
//     if (!arr.includes(a[i]))
//         {arr.push(a[i])} 
    
//     else{arr1.push(a[i])}
// }
// // console.log(arr,arr1)

// arr = [5, 6, 1, 2, 3, 4, 7, 9, 8];

// for (let i = 0; i < arr.length - 1; i++) {               #sorting the array

//     for (let j = i + 1; j < arr.length; j++) {

//         if (arr[i] > arr[j]) {
        
//             let temp = arr[i];
//             arr[i] = arr[j];
//             arr[j] = temp;
//         }
//     }
// }

// console.log(arr); // Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]





// let n = 10
// let a = 0;
// let b = 1;                                   #Nth  Fibonacci
// let fib;

// if (n === 0) {
//     fib = a; // The 0th Fibonacci number is 0
// } else if (n === 1) {
//     fib = b; // The 1st Fibonacci number is 1
// } else {
//     for (let i = 2; i <= n; i++) {
//         fib = a + b;  // Current Fibonacci number
//         a = b;        // Move to next number
//         b = fib;      // Move to next number
//     }
// }

// console.log(fib); // Output the result
