let a = ["cdab", "dcba", "abcd"];
let b = ["abcd", "abcd", "abcdcd"];
let result = [];

for (let i = 0; i < a.length; i++) {
    let a_element = a[i];
    let b_element = b[i];

    if (a_element.length !== b_element.length) {
        result.push("No");
    } else {
        let a_odd = [],
            a_even = [],
            b_odd = [],
            b_even = [];

        for (let j = 0; j < a_element.length; j++) {
            if (j % 2 == 0) {
                a_even.push(a_element[j]);
                b_even.push(b_element[j]);
            } else {
                a_odd.push(a_element[j]);
                b_odd.push(b_element[j]);
            }
        }

        if (a_even.sort().join() === b_even.sort().join() &&
            a_odd.sort().join() === b_odd.sort().join()) {
            result.push("Yes");
        } else {
            result.push("No");
        }
        console.log('i', i)
        console.log(a_even, b_even, a_odd, b_odd);
    }
}

console.log(result);