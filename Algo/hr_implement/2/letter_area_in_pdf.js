function designerPdfViewer(h,word) {
    let width = word.length,
        word_height =[];
    
    word.split('').forEach(element => {        
        word_height.push(h[element.charCodeAt()-97]);
    });
    return (Math.max(...word_height)) * width;
}

let h = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'.split(' ').map(Number),
	word = 'zaba';

console.log(designerPdfViewer(h, word));