var crypto = require('crypto');

console.log(crypto.getHashes());

const fs = require('fs');

const testfile = fs.readFileSync('test.cpp');
var sha1sum = crypto
  .createHash('sha1')
  .update(testfile)
  .digest('hex');
console.log(sha1sum);
