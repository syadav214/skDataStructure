function getMoneySpent(keyboards, drives, b) {
    let money_spent = 0;
    for (i in keyboards) {
        for (j in drives) {
            let sum_keyboard_drives = keyboards[i] + drives[j];
            if (sum_keyboard_drives <= b) {
                money_spent = Math.max(money_spent, sum_keyboard_drives);
            }
        }
    }

    return money_spent;
}

let keyboards = [3, 1],
    drives = [5, 2, 8],
    b = 10;
console.log(getMoneySpent(keyboards, drives, b));