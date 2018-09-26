'use strict';

/* global CustomError, getLikedBrands, getTopBrandsForGender */

function solution(U, N) {
  return new Promise((resolve, reject) => {
    Promise.all([getLikedBrands(U.id), getTopBrandsForGender(U.gender)])
      .then(brandArray => {
        let finalBrand = [];
        let allBrands = [];

        if (brandArray[1].length > 0) {
          allBrands = brandArray[0];

          if (brandArray[1].length > 0) {
            for (let i = 0; i < brandArray[1].length; i++) {
              // Checking current brand id exists in allBrands
              let brndExists = allBrands.find(
                brnd => brnd.id === brandArray[1][i].id
              );

              // push the brand data if it does not exist
              if (brndExists == null) {
                allBrands.push(brandArray[1][i]);
              }
            }
          }
        } else if (brandArray[1].length > 0) {
          allBrands = brandArray[1];
        }

        if (N > allBrands.length) {
          return reject(new CustomError('Not enough data'));
        } else {
          for (let i = 0; i < N; i++) {
            finalBrand.push(allBrands[i].name);
          }
        }

        return resolve(finalBrand);
      })
      .catch(err => {
        console.log('Error:', err);
      });
  });
}
