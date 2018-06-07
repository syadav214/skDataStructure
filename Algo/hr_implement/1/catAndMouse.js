function catAndMouse(x,y,z) {
    let diff_x_z = Math.abs(x - z),
    diff_y_z =  Math.abs(y-z);

    if(diff_x_z === diff_y_z) {
        return 'Mouse C';
    } else if(diff_x_z < diff_y_z) {
        return 'Cat A';
    } else {
        return 'Cat B';
    }

}

console.log(catAndMouse(1,2,3));