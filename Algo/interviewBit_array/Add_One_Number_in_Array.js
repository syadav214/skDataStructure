var newString = "";

for (var i = 0; i < A.length; i++) {
    newString = newString + A[i].toString();
}

newString = (parseFloat(newString) + 1).toString();

var newArray = [];

newString.split("").forEach(function(n) {
    newArray.push(parseFloat(n));
});

return newArray;