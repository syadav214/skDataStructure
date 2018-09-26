// ExponentialBackoff=> sending request to resend after a failed attempt. such as 2 then 2pow2 = 4 then 2pow3 = 8 then 2pow4 = 16
async function sendWithExponentialBackoff(emails) {
  // Example: to send the first email in the array, call send(emails[0])
  let successEmailCount = 0,
    failEmailCount = 0,
    waitSec = 1000;
  for (let i = 0; i < emails.length; i++) {
    let status = false,
      failCount = 0;
    while (!status) {
      try {
        status = await sendEmail(emails[i]);
      } catch (err) {
        status = false;
      }

      if (!status) {
        failCount++;
        sleep(waitSec);
        waitSec = waitSec * 2;
      }
      if (failCount == 10) {
        failEmailCount++;
        status = true;
        break;
      }
    }

    if (failCount < 10) {
      successEmailCount++;
    }
    waitSec = 1000;
  }
  return new Promise(function(resolve, reject) {
    if (successEmailCount == emails.length) {
      resolve('Successful');
    } else {
      reject(new Error(failEmailCount + ' emails failed to send'));
    }
  });
}

function sleep(ms) {
  return new Promise(resolve => {
    setTimeout(resolve, ms);
  });
}

async function sendEmail(emailid) {
  return new Promise(function(resolve, reject) {
    send(emailid)
      .then(result => {
        resolve(true);
      })
      .catch(err => {
        reject(false);
      });
  });
}
