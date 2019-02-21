let a = {
  userRecommend: [
    {
      Date: '2018-07-25',
      Price: 10
    }
  ]
};

if (a.userRecommend && a.userRecommend.length > 0 && a.userRecommend[0].Price) {
  console.log(a.userRecommend[0].Price);
} else {
  console.log('not recom');
}
