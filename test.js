function saveThePrisoner(nOfPrisoners, candies, startingPoint) {
    let a = 0;
    a = ((startingPoint-1) + candies) % nOfPrisoners;

    if(a==0) {
        return nOfPrisoners;
    } else {
        return a;
    }
}

console.log(saveThePrisoner(5,2,1));