function angryProfessor(k,a) {
    let on_timers = 0;

    a.forEach(element => {
        if(element < 1) {
            on_timers++;
        }
    });
    
    if(on_timers>=k){
        return 'No';
    } else{
        return 'Yes';
    }
}

let k =2,
    a = '0 -1 2 1'.split(' ').map(Number);

console.log(angryProfessor(k,a));

