const crypto = require('crypto');
const fs = require('fs');
//console.log(crypto.getHashes());

const testfile = fs.readFileSync('kaprekarNumbers.cpp');
const sha1sum = crypto
  .createHash('sha1')
  .update(testfile)
  .digest('hex');
console.log(sha1sum);
