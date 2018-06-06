function climbingLeaderboard(scores, alice) {
    let result = [];
    let x =  new Set(scores);
    let y = [...x];
    let len = y.length + 1,
        high = 0,
        low = 0,
        mid = 0,
        rank = 0;

    
    //descending sort
    //y.sort(function(a, b){return b-a});

    //ascending sort
    y.sort(function(a, b){return a-b});
    
    alice.forEach(element => {
        
        rank = len;
        high = len -1;
        
        while(low < high) {            
            mid = Math.floor((low+high)/2);
            if(y[mid] <= element) {             
                low = mid +1;
            } else {
                high = mid;
            }
        }
        rank -= low;
        result.push(rank);
    });
    

    return result;
}

let scores = [100, 100, 50, 40, 40, 20, 10],
    alice = [5, 25, 50, 120];

console.log(climbingLeaderboard(scores,alice));
