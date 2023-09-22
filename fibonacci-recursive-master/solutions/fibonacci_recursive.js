/**
 * The above code defines a recursive function called `fibonacci` that calculates the Fibonacci
 * sequence for a given number `n`, and includes some test cases to verify its correctness.
 * @param n - n is the input number for which we want to calculate the Fibonacci sequence.
 * @returns The function `fibonacci(n)` returns the nth number in the Fibonacci sequence.
 */
function fibonacci(n) {
  if (n < 2) {
    return n;
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
}

if (require.main === module) {
  // add your own tests in here
  console.log(fib(3)); //2
  console.log(fib(5)); //5
  console.log(fib(8)); //21

  console.log("Expecting: 0");
  console.log(fibonacci(0));

  console.log("");

  console.log("Expecting: 1");
  console.log(fibonacci(2));

  console.log("");

  console.log("Expecting: 55");
  console.log(fibonacci(10));

  console.log("");

  console.log("Expecting: 1");
  console.log(fibonacci(1));

  console.log("");

  console.log("Expecting: 6765");
  console.log(fibonacci(20));
}

module.exports = fibonacci;

/* The code is defining a recursive function called `fibo` that calculates the Fibonacci sequence. */

function fibo(n) {
  if(n < 2) {
    return n;

  }
  return fibo(n-1) + fibo(n-2); // Fn-1 + Fn-2

}


/**
 * The function calculates the nth Fibonacci number using memoization to store previously calculated
 * values.
 * @param n - The parameter `n` represents the index of the Fibonacci number to calculate. It is the
 * position of the number in the Fibonacci sequence.
 * @param memo - The `memo` parameter is an object that is used to store previously calculated
 * Fibonacci numbers. It is initially passed as an empty object `{}` and is used to avoid redundant
 * calculations by storing and reusing previously calculated values.
 * @returns the nth Fibonacci number.
 */
function fib(n, memo) {
  if (n < 2) {
    return n;
  }
  if(!memo[n]) {
    // when the object doesn't have the property of n
    // store the result of the call inside memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
  }
  return memo[n];
}

console.log(fib(5, {})); // 5


// Please add your pseudocode to this file
/**The code is defining a recursive function called `fibo` that calculates the Fibonacci sequence. */

 /* The above code defines a recursive function called `fibonacci` that calculates the Fibonacci
 * sequence for a given number `n`, and includes some test cases to verify its correctness.
 * @param n - n is the input number for which we want to calculate the Fibonacci sequence.
 * @returns The function `fibonacci(n)` returns the nth number in the Fibonacci sequence.
 */
/**
 * The function calculates the nth Fibonacci number using memoization to store previously calculated
 * values.
 * @param n - The parameter `n` represents the index of the Fibonacci number to calculate. It is the
 * position of the number in the Fibonacci sequence.
 * @param memo - The `memo` parameter is an object that is used to store previously calculated
 * Fibonacci numbers. It is initially passed as an empty object `{}` and is used to avoid redundant
 * calculations by storing and reusing previously calculated values.
 * @returns the nth Fibonacci number.
 */
/************************************************************************************** 
* if n is less than 2 return n
*
* return last value in sequence + second to last value in sequence
***************************************************************************************/

// And a written explanation of your solution
/************************************************************************************** 
* We can use the same base case as the iterative version: if n is less than 2, just
* return n, since 0 and 1 are the first values in the series. After that we need to
* calculate the next value by adding up the two previous values. If we recurse until
* n equals 0 or 1, we'll hit the base case and start returning values, which can then
* be added together. For example, if we start with n = 2, our recursive call will be
* fibonacci(1) + fibonacci(0). Both sides of the equation will hit the base case. The 
* left side will return 1 and the right side will return 0, resulting in a total of 1.
***************************************************************************************/
