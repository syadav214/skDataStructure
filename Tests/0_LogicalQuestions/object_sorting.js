const activity = [
    { name: 'a1', start: 0, end: 2 },
    { name: 'a2', start: 3, end: 4 },
    { name: 'a3', start: 1, end: 2 },
    { name: 'a4', start: 5, end: 9 },
    { name: 'a5', start: 5, end: 7 },
    { name: 'a6', start: 8, end: 9 }
  ];
  
  activity.sort((a, b) => a.start - b.start);
  
  console.log(activity[0].name);
  let prevEnd = activity[0].end;
  
  for (let i = 1; i < activity.length; i++) {
    if(activity[i].start > prevEnd) {
      console.log(activity[i].name);
      prevEnd = activity[i].end;
    }
  }
  
  
  //compare each finish with next start and print
  
  //https://www.youtube.com/watch?v=poWB2UCuozA
  