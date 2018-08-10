const fs = require('fs');

function saveEmails(emails, cb) {
  let successfullySavedFiles = [],
    errors = [];
  for (let i = 0; i < emails.length; i++) {
    let singleEmail = emails[i];
    try {
      fs.writeFileSync(singleEmail, singleEmail, {
        encoding: 'utf8'
      });
      successfullySavedFiles.push(singleEmail);
    } catch (err) {
      errors.push(err);
    }
    /*
        fs.writeFile(fileName, singleEmail, 'utf8', err => {
          if (err) errors.push(err);
          console.log('1');
          successfullySavedFiles.push(singleEmail);
        });
        */
  }

  //console.log('2');
  if (errors.length == 0) {
    cb(null, successfullySavedFiles);
  } else {
    cb(errors, null);
  }
}
