function BreakingRecords(score) {
    let min_score = score[0],
        max_score = score[0],
        min_cnt = 0,
        max_cnt = 0;

    for (let i = 0; i < score.length; i++) {
        if (min_score > score[i]) {
            min_score = score[i];
            min_cnt++;
        }

        if (max_score < score[i]) {
            max_score = score[i];
            max_cnt++;
        }
    }

    return [max_cnt, min_cnt];
}

let a = [10, 5, 20, 20, 4, 5, 2, 25, 1];
console.log(BreakingRecords(a));