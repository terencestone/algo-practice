input = [[0,0], [1,2], [2,3], [2,2], [3,1], [3,3]] //==> 3

function findGreatestStraightLine(arr) {

    if (arr === null || !arr.length) { return 0 }
    if (arr.length === 1) { return 1 }

    // we know that if we got here, the max will be at least 2
    let max_slope = 2
    // iterate through each set of coordinates
    for (let i = 0; i < arr.length; i++) {
      // initialize dupes as 1 to account for original point in slope
      let dupes = 1
      // each time, declare the dictionary with an empty key in case of empty dict
      let slope_dict = {}
      // compare subsequent coords for with nested iteration
      for (let j = i+1; j < arr.length; j++) {
        // the coordinates are exactly the same, just add as duplicate
        if (arr[i][0] === arr[j][0] && arr[i][1] === arr[j][1]) {
          dupes++
        }
        else {
          // calculate the slope
          let curr_slope = (arr[j][1] - arr[i][1]) / (arr[j][0] - arr[i][0])
          // add it to the dictionary
          slope_dict[curr_slope] = slope_dict[curr_slope] ? slope_dict[curr_slope] + 1 : 1
        }
      }
      // for each of the outer iterations compare max slope of current slope_dict to the current max_slope
      for (let k in slope_dict) {
        // new max_slope is the largest number + value of dupes (defaults to 1)
        if (slope_dict[k] + dupes > max_slope) {
          max_slope = slope_dict[k] + dupes
        }
      }
    }

    return max_slope;
}

console.log(findGreatestStraightLine(input))

/* ORIGINAL BELOW */

// console.log("testing")

// Given an array of integers ordered 0 - 51 and a good random function, “shuffle” the array. That is, manipulate elements in the array such that the array’s elements appear to be random order.

// const getRandomInt = max => Math.floor(Math.random()*max)


// // function range(start, edge, incr) {
// //     if (arguments.length === 1) {
// //         edge = start;
// //         start = 0;
// //     }

// //     edge = edge || 0;
// //     step = step || 1;

// //     let arr = []
// //     for (arr; (edge - start) * step > 0; start += step) {
// //         arr.push(start)
// //     }

// //     return arr;
// // }

// function shuffle(arr) {
//     for (let i = 0; i < arr.length; i++){
//         let j = getRandomInt(arr.length)
//         let first = arr[i]
//         arr[i] = arr[j]
//         arr[j] = first
//     }

//     return arr;
// }

// input = [1,2,3,4,5]

// console.log(shuffle(input))

// As an input, you have points on a 2D graph. You aim to find a straight line that can fit as my points as possible. Return the maximum number of points you can fit.

// input = [[0,0], [1,2], [2,3], [2,2], [3,1], [3,3]] //==> 3

// let slope = y1-y / x1-x

// function findGreatestStraightLine(arr) {
//     let slope_dict = {}
//     for (let i = 0; i < arr.length; i++) {
//         for (let j = i+1; j < arr.length; j++) {
//             let curr_slope = (arr[j][1] - arr[i][1]) / (arr[j][0] - arr[i][0])
//             if (!slope_dict[curr_slope]) {
//                 slope_dict[curr_slope] = 1
//             } else {
//                 slope_dict[curr_slope] += 1
//             }
//         }
//     }

//     let max = 0
//     for (let k in slope_dict) {
//         if (slope_dict[k] > max) {
//             max = slope_dict[k]
//         }
//     }

//     return max;
// }

// console.log(findGreatestStraightLine(input))