const arr = [1, 2, 3, 3, 2, 2, 4, 5, 1, 4, 6];

// using sets
console.log(new Set(arr));

// using Map
const unique = [];
const uniqueMap = new Map();

arr.map(ele=> {
    if(!uniqueMap[ele]) {
        uniqueMap[ele] = ele;
        unique.push(ele);
    }
});

console.log(uniqueMap,unique);

/* arr.forEach and arr.map 
forEach: This iterates over a list and applies some operation with side effects to each list member 
(example: saving every list item to the database)

map: This iterates over a list, transforms each member of that list, and 
returns another list of the same size with the transformed members
 (example: transforming list of strings to uppercase)
*/