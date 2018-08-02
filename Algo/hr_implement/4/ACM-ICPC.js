function acmTeam(obs) {
  let known = 0,
    max_known = 0,
    know_all = 0;

  for (let i = 0; i < obs.length; i++) {
    for (let j = i + 1; j < obs.length; j++) {
      known = 0;
      for (let k = 0; k < obs[j].length; k++) {
        if (obs[i][k] == '1' || obs[j][k] == '1') {
          known++;
        }

        if (known > max_known) {
          max_known = known;
          know_all = 0;
        }

        if (known == max_known) {
          know_all++;
        }
      }
    }
  }

  return { max_known, know_all };
}

let obs = ['10101', '11110', '00010', '00101'];
console.log(acmTeam(obs));
