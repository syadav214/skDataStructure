function extraLongFactorials(n) {
    let multi=1, x=n;
    for(i=0;i<n-1;i++){        
        multi = multi * x;
        x = x - 1;
    }
    return multi;
}

console.log(extraLongFactorials(5));