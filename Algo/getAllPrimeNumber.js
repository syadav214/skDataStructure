//Given a number N, N>=2. Print all prime numbers <= N.

class Prime {
    getPrimeNumber(n) {
        var arrayOfPrime = [];
        var i = 2;
        while (n >= i) {
            if (this.checkPrime(i)) {
                arrayOfPrime.push(i);
            }
            i++;
        }
        return arrayOfPrime;
    }

    checkPrime(n) {
        var isItPrime = true;
        for (var i = 2; i < n; i++) {
            if (n % i == 0) {
                isItPrime = false;
                break;
            }
        }
        return isItPrime;
    }
}

var p = new Prime();
console.log(p.getPrimeNumber(10));