/*
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.
For example, assume her scores for the season are represented in the array . 
Scores are in the same order as the games played. She would tabulate her results as follows:
*/

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