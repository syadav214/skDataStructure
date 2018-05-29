function sockMerchant(ar) {
    let pair_hash = {},
        count = 0;
    for (i in ar) {
        if (ar[i] in pair_hash) {
            count++;
            delete pair_hash[ar[i]];
        } else {
            pair_hash[ar[i]] = 1;
        }
    }

    console.log(count);
}

let ar = [10, 20, 20, 10, 10, 30, 50, 10, 20];
sockMerchant(ar);