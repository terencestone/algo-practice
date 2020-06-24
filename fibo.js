const getNthFiboPrimes = (n) => {
  if (n <= 2) { return [] }
  list = getFibo(n)
  return getPrimes(list)
}

const getFibo = (n) => {
  if (n===1) {
    return [0, 1];
  }
  else {
    var s = getFibo(n - 1);
    s.push(s[s.length - 1] + s[s.length - 2]);
    return s
  }
}

const getPrimes = (arr) => {
  primeNumArray = arr.filter((number) => {
    if (number <= 1 ) { return false }
    for (var i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) return false;
    }
    return true;
  });
  return primeNumArray
}

// solution(0)
console.log(getNthFiboPrimes(1))
console.log(getNthFiboPrimes(2))
console.log(getNthFiboPrimes(3))
console.log(getNthFiboPrimes(4))
console.log(getNthFiboPrimes(5))
console.log(getNthFiboPrimes(6))
console.log(getNthFiboPrimes(7))