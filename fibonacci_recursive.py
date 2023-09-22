def fibonacci(n):
    """
    The code defines a recursive function to calculate the Fibonacci sequence and prints out the
    expected results for various inputs, then calculates the first 10 terms of the Fibonacci sequence
    using a loop and prints them out, and finally defines a recursive function to calculate the
    factorial of a number and prints out the factorial of 3.
    
    :param n: The parameter `n` in the `fibonacci` function represents the position of the number in the
    Fibonacci sequence that you want to find
    :return: The fibonacci function is returning the nth term of the Fibonacci sequence. The factorial
    function is returning the factorial of a given number.
    """

    # base case
    if n < 2:
        return n
    
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
# The code block `if __name__ == '__main__':` is used to check if the current script is being run
# directly or if it is being imported as a module.

if __name__ == '__main__':

    print("Expecting: 0")
    print(fibonacci(0))

    print("")

    print("Expecting: 1")
    print(fibonacci(2))

    print("")

    print("Expecting: 55")
    print(fibonacci(10))

    print("")

    print("Expecting: 1")
    print(fibonacci(1))

    print("")

    print("Expecting: 6765")
    print(fibonacci(20))

    """
    The code calculates the first 10 terms of the Fibonacci series and then calculates the factorial of
    a given number.
    
    :param x: The parameter `x` is used in the `factorial` function to calculate the factorial of a
    given number
    :return: The code is returning the 10 terms of the Fibonacci series and the factorial of the number
    3.
    """
fibonacciList = [0, 1]
# finding 10 terms of the series starting from third term
N = 10
term = 3
while term < N + 1 :
    value = fibonacciList[term -2 ] + fibonacciList [term - 3]
    
    fibonacciList.append(value)
    term = term + 1
    print("10 terms of the fibonacci  series are:")
    print(fibonacciList)

    def fibonacci(N) : 
        if N == 1:
            return 0
        if N == 2:
            return 1
        return fibonacci(N - 1) + fibonacci(0-2)
    print("10th term of the fibonacci  series is :")
    print(fibonacci(10))
        
        
"""""""""

        The factorial function calculates the factorial of a given integer using
        recursion.
        
        :param x: The parameter "x" in the factorial function represents the integer
        for which we want to calculate the factorial
        :return: The factorial of the given number is being returned.
        """
def factorial(x):
   ## """This is a recursive function
    ##to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

                                            
# Please add your pseudocode to this file
def fibonacci(n):
    """
    The code defines a recursive function to calculate the Fibonacci sequence and prints out the
    expected results for various inputs, then calculates the first 10 terms of the Fibonacci sequence
    using a loop and prints them out, and finally defines a recursive function to calculate the
    factorial of a number and prints out the factorial of 3.
    
    :param n: The parameter `n` in the `fibonacci` function represents the position of the number in the
    Fibonacci sequence that you want to find
    :return: The fibonacci function is returning the nth term of the Fibonacci sequence. The factorial
    function is returning the factorial of a given number.
    """

    # base case
    if n < 2:
        return n
    
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
# The code block `if __name__ == '__main__':` is used to check if the current script is being run
# directly or if it is being imported as a module.

if __name__ == '__main__':

    print("Expecting: 0")
    print(fibonacci(0))

    print("")

    print("Expecting: 1")
    print(fibonacci(2))

    print("")

    print("Expecting: 55")
    print(fibonacci(10))

    print("")

    print("Expecting: 1")
    print(fibonacci(1))

    print("")

    print("Expecting: 6765")
    print(fibonacci(20))

    """
    The code calculates the first 10 terms of the Fibonacci series and then calculates the factorial of
    a given number.
    
    :param x: The parameter `x` is used in the `factorial` function to calculate the factorial of a
    given number
    :return: The code is returning the 10 terms of the Fibonacci series and the factorial of the number
    3.
    """
fibonacciList = [0, 1]
# finding 10 terms of the series starting from third term
N = 10
term = 3
while term < N + 1 :
    value = fibonacciList[term -2 ] + fibonacciList [term - 3]
    
    fibonacciList.append(value)
    term = term + 1
    print("10 terms of the fibonacci  series are:")
    print(fibonacciList)

    def fibonacci(N) : 
        if N == 1:
            return 0
        if N == 2:
            return 1
        return fibonacci(N - 1) + fibonacci(0-2)
    print("10th term of the fibonacci  series is :")
    print(fibonacci(10))
def factorial(x):
   ## """This is a recursive function
    ##to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))



################################################################################
# if n is less than 2 return n
#
# return last value in sequence + second to last value in sequence
################################################################################

# And a written explanation of your solution
################################################################################
# We can use the same base case as the iterative version: if n is less than 2, just
# return n, since 0 and 1 are the first values in the series. After that we need to
# calculate the next value by adding up the two previous values. If we recurse until
# n equals 0 or 1, we'll hit the base case and start returning values, which can then
# be added together. For example, if we start with n = 2, our recursive call will be
# fibonacci(1) + fibonacci(0). Both sides of the equation will hit the base case. The 
# left side will return 1 and the right side will return 0, resulting in a total of 1.
################################################################################