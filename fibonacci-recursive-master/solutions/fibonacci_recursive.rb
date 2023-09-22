def fibonacci(n)
  return n if n < 2

  fibonacci(n - 1) + fibonacci(n - 2)
end

if __FILE__ == $PROGRAM_NAME
  puts "Expecting: 0"
  puts fibonacci(0)

  puts

  puts "Expecting: 1"
  puts fibonacci(2)

  puts

  puts "Expecting: 55"
  puts fibonacci(10)

  # Don't forget to add your own!
  puts

  puts "Expecting: 6765"
  puts fibonacci(20)

  puts

  puts "Expecting: 1"
  puts fibonacci(1)
end




def fibonacci(n)
  return n if n < 2

  values = [0, 1]

  (n - 1).times do
    values << values[-1] + values[-2]
  end

  values.last
end

##

def fibonacci_recursively(n)
  if n > 2
      return (fibonacci_recursively(n-1) +fibonacci_recursively(n-2))
  end
end



# Please add your pseudocode to this file
# The above function calculates the nth Fibonacci number using an iterative approach.
# 
# Args:
#   n: The parameter "n" in the above code represents the position of the Fibonacci number that we
# want to calculate. For example, if we pass 5 as the value of "n", the code will calculate the 5th
# Fibonacci number.
# 
# Returns:
#   the nth Fibonacci number.


# The function calculates the nth Fibonacci number recursively.
# 
# Args:
#   n: The parameter "n" represents the position of the Fibonacci number in the sequence that we want
# to find.
# 
# Returns:
#   the nth number in the Fibonacci sequence.

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
