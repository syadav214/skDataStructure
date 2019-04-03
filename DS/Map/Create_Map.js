var myHash = new Map();
myHash['one'] = [1, 10, 5];
myHash['two'] = [2];
myHash['three'] = [3, 30, 300];
console.log(myHash['three']);

myHash.set('four',[4,4,4,4])
console.log(myHash.get('four'));

var myHash_Object = {}; // New object
myHash_Object['one'] = [1, 10, 5];
myHash_Object['two'] = [2];
myHash_Object['three'] = [3, 30, 300];

console.log(myHash_Object);

//deleting a key
delete myHash_Object['one'];
