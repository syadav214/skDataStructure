function countingValleys(n, s) {
    let curr_level = 0,
        vally_counter = 0,
        below_sea_level = false;

    for (i in s) {
        if (s[i] == "U") {
            curr_level++;
        } else {
            curr_level--;
        }

        if (below_sea_level == false) {
            if (curr_level < 0) {
                below_sea_level = true;
            }
        } else if (curr_level == 0) {
            below_sea_level = false;
            vally_counter++;
        }
    }

    return vally_counter;
}

console.log(countingValleys(10, 'UDUUUDUDDDT'));