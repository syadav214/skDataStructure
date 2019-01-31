const s = new Date().getSeconds();

setTimeout(function() {
    console.log('Executed');
},500);

while(true) {
    if(new Date().getSeconds() - s >= 2) {
        break;
    }
}

/*
Q => After how many seconds it will print 'Executed'
A => 2 sec. (not 500 ms). Because, setTimeout will be in queue and while loop will be on stack. After while loop finished console log executes.
*/
