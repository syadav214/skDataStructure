function beautifulDays(i, j, k) {
    let count =0;
    for(let x = i;x<=j;x++){
        let reverse_number = x.toString().split('').reverse();
        reverse_number = parseInt(reverse_number.join(''));
        
        if((Math.abs(x-reverse_number)) % k ==0) {
            count++;
        }
    }
    
    return count;
}

console.log(beautifulDays(20,23,6));