const fs = require('fs');

let rawdata = fs.readFileSync('blogData.json');
let student = JSON.parse(rawdata);
for (let s in student) {
  fs.writeFileSync('test/' + s, student[s]);
  //console.log(s,student[s]);
}
