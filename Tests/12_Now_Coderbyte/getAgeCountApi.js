const https = require("https");

https.get("https://coderbyte.com/api/challenges/json/age-counting", (resp) => {
  let data = "";

  resp.on("data", function (chunk) {
    data += chunk;
  });

  resp.on("end", function () {
    let count = 0;
    const arr = data.split(",");
    arr.forEach((e) => {
      let single = e.trim();
      const valArr = single.split("=");
      if (valArr[0] === "age") {
        const age = parseInt(valArr[1]);
        if (age > 49) {
          count++;
        }
      }
    });
    console.log(count);
  });
});
