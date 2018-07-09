function jumpingOnClouds(c,k) {
    let E = 100;
    for(let i=0;i<c.length;i = i+k) {
        let subVal=1;
        if (c[i]==1){
            subVal +=2;
        }
        E = E - subVal;
    }
    return E;
}

let c = [0, 0, 1, 0, 0, 1, 1, 0]
	k = 2;

console.log(jumpingOnClouds(c,k));