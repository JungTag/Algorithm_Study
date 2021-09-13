function power(a, n) {
    if (n === 0) {
        return 1;
    }

    let x = power(a, n/2);

    if (n%2 === 0) {
        return x * x;
    } else {
        return x * x * a;
    }
}

console.log(power(2, 3));