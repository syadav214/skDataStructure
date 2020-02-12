const fs = require('fs');
const allFolderName = [];
fs.readFile('test2.csv', (err, data) => {
  const filedata = data.toString().split('\n');
  filedata.map(ele => {
    const singleEleArr = ele.split(',');
    if (singleEleArr[1] && singleEleArr[1].indexOf('/') > 0) {
      const folderName = singleEleArr[1].substring(
        0,
        singleEleArr[1].indexOf('/')
      ).replace(`"`,'');
      if (allFolderName.includes(folderName) === false) {
        allFolderName.push(folderName);
      }
    }
  });
  console.log(allFolderName);
});
