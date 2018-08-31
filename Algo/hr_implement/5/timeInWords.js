let hours = [
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
  'ten',
  'eleven',
  'twelve',
  'thirteen',
  'fourteen',
  'fifteen',
  'sixteen',
  'seventeen',
  'eighteen',
  'nineteen'
];

let minutes = [
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
  'ten',
  'eleven',
  'twelve',
  'thirteen',
  'fourteen',
  'fifteen',
  'sixteen',
  'seventeen',
  'eighteen',
  'ninteen',
  'twenty',
  'twenty one',
  'twenty two',
  'twenty three',
  'twenty four',
  'twenty five',
  'twenty six',
  'twenty seven',
  'twenty eight',
  'twenty nine'
];

function timeInWords(h, m) {
  let timeWords = '';

  if (m == 0) {
    timeWords = hours[h] + " o' clock";
  } else if (m == 15) {
    timeWords = 'quarter past ' + hours[h];
  } else if (m < 30) {
    timeWords = minutes[m] + ' ';
    if (m == 1) {
      timeWords += 'minute';
    } else {
      timeWords += 'minutes';
    }
    timeWords += ' past ' + hours[h];
  } else if (m == 30) {
    timeWords = 'half past ' + hours[h];
  } else if (m == 45) {
    timeWords = 'quarter to ' + hours[h + 1];
  } else {
    let diffMin = 60 - m;
    timeWords = minutes[diffMin] + ' ';
    if (diffMin == 1) {
      timeWords += 'minute';
    } else {
      timeWords += 'minutes';
    }
    timeWords += ' to ' + hours[h + 1];
  }

  return timeWords;
}

console.log('Ans:', timeInWords(5, 0));
