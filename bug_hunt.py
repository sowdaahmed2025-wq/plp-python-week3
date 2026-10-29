count = 1
total = 0

# BUG: The while line was missing a colon at the end, which caused a SyntaxError. I added the colon.
# BUG: The condition count < 5 stopped the loop before adding 5, so the sum was 10 instead of 15. I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: I tried to join a string and an integer with +, which caused a TypeError. I wrapped total in str() to convert it to text.
print("Sum of 1 to 5 is: " + str(total))
