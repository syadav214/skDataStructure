/*
Install mocha with globally accessiable to run test Cases
Install request to request WebAPI
Install chai to compare excepted result with actual result
mocha test.js
*/
var request = require("request");
var except = require("chai").expect;
var baseurl = "http://localhost:3000/";

describe('MyProject', function() {
    it('MyModule', function(done) {
        request.get({ url: baseurl },
            function(err, res, body) {
                except(res.statusCode).to.equal(200);
                console.log(body);
                done();
            }
        );
    });
});