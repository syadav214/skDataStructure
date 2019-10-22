//1. arrow function
const a = () => {}
//2. lenght
let str= '1111';
console.log(str.length)
//3. switch case
var x = 2;
var number = 10;
switch(x) {
    case 1:
        number = number + 1;
        break;
    case 2:
        number = number - 3;
    case 3:
        number = number + 10;
        break;
}
console.log(number);

//4. array length
var arr = [];
arr.push('arr');
arr[10] = '12';
arr[10] = undefined;
arr[5] = 'b';
console.log(arr.length)

//5. assign object
var obj1 = {a:1,b:2};
var obj2 = obj1;
obj2.a = 42;
delete obj2.b;
console.log(obj1.a,obj1.b);

//6. String index
let str1 = 'hshhhs dhhdhydjdkkd';
str1[1] = '2';
console.log(str1[1])