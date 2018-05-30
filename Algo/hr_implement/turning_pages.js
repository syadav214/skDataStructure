function pageCount(n, p) {
    return Math.floor(Math.min(p / 2, (n / 2 - p / 2)));
}

console.log(pageCount(5, 4));