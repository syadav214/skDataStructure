function utopianTree(n) {
    let height =1;   
    if(n>0)   {
        for(let i=1;i<=n;i++){
            if(i%2==0){
                height++;
            } else{
                height = height*2;
            } 
        }
    }    
    return height;
}

console.log(utopianTree(4));