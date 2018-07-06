function permutationEquation(p) {
    let result = [];
    for(let i=0;i<p.length;i++) {
        let x = i + 1;
        let index = p.indexOf(x);
        x = p.indexOf(index + 1);
        result.push(x+1)
    }
    return result;
}

let p = [2,3,1];
console.log(permutationEquation(p));