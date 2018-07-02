function viralAdvertising(n){
    let ads=5,
    likes=0,
    refer = 3;

    for(let i=1;i<=n;i++){
        let tmp_like = Math.floor(ads/2);
        likes += tmp_like;
        ads = tmp_like*refer;
    }
    return likes;
}

console.log('likes',viralAdvertising(3));