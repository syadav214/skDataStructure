var requestify = require('requestify');

function request_chunk(callID) {
    console.log('request_chunk:', callID);

    requestify.request('http://localhost:3005', {
            method: 'POST',
            body: {
                call: callID
            },
            dataType: 'json'
        })
        .then(function successCallback(response) {
            console.log('succeeded', response.body);
        }, function errorCallback(response) {
            console.log('failed', response);
        });
}

for (i = 0; i < 1000; i++) {
    if (i == 800) {
        throw 'Test';
    }
    request_chunk(i);
}



//Stream code in chunk_Streams.js