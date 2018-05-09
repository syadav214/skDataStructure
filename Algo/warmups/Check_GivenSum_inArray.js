B = [1, 2, 7, 9];
//B = [1, 2, 4, 4];
sum = 8;

var hashTable = {};
var matched = false;
for (var i in B) {

    let comp = sum - B[i];
    if (comp in hashTable) {
        matched = true;
        break;
    }
    hashTable[comp] = i;
}

console.log('matched', matched);