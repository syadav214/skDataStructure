function circularArrayRotation(a, k, queries) {
    let result=[],array_a_len = a.length;

    for(let i=0;i<queries.length;i++){
        let index = ((queries[i]- k) % array_a_len);        
        result.push(a[index]);
    }
    return result;
}

let a = [1, 2, 3],
k = 2,
queries = [0,1,2];

console.log(circularArrayRotation(a,k,queries));