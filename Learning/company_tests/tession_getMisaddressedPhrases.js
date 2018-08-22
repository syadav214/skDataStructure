function getMisaddressedPhrases(message_text) {
  /* 
      misaddressed phrase list: 
      I'm sorry,  accidentally sent, misaddressed, not meant for, wrong address, please delete, wrong person
    */
  let misaddressedWords = [];
  let phraseList = [
    [`Im`, `sorry`],
    [`accidentally`, `sent`],
    [`misaddressed`],
    [`not`, `meant`, `for`],
    [`wrong`, `address`],
    [`please`, `delete`],
    [`wrong`, `person`]
  ];

  message_text = message_text.replace(/[^a-zA-Z ]/g, '');

  let arrMessage_text = message_text.split(' ');

  for (let i = 0; i < arrMessage_text.length; i++) {
    let currWord = arrMessage_text[i];
    let foundWordInPhrase = phraseList.filter(el => el[0] == currWord);

    if (foundWordInPhrase.length > 0) {
      if (foundWordInPhrase[0].length == 1) {
        misaddressedWords.push(element);
      } else {
        for (let j = 0; j < foundWordInPhrase.length; j++) {
          if (arrMessage_text.length > foundWordInPhrase[j].length + i - 1) {
            let wordsFromMessage = arrMessage_text
              .slice(i, foundWordInPhrase[j].length + i)
              .join(' ');

            let wordsFromPhrase = foundWordInPhrase[j].join(' ');

            if (wordsFromMessage === wordsFromPhrase) {
              misaddressedWords.push(wordsFromMessage);
            }
          }
        }
      }
    }
  }

  if (misaddressedWords.length == 0) {
    misaddressedWords.push('No flags');
  }

  return misaddressedWords;
}

let message_text =
  "I'm hi santosh this is life and beyond it we belive I'm sorry";
//"hi santosh this is life and beyond it we belive I'm sorry and what about wrong address and wrong person hey not meant for you.";
//'Sorry Karen - I accidentally sent this to the wrong person..';
console.log(getMisaddressedPhrases(message_text));
