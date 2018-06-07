function pickingNumbers(a) {
    let max = 0;

    a.forEach(element => {
        let count_curr = a.filter(x=>x==element).length,
            count_curr_minus_one = a.filter(x=> x==element-1).length,
            sum_of_counts = count_curr + count_curr_minus_one;

        if(sum_of_counts > max) {
            max = sum_of_counts;
        }
    });

    return max;
}

let a = [1, 2, 2, 3, 1, 2];

console.log(pickingNumbers(a));
