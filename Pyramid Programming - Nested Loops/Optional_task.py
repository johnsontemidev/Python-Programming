# ============ INTRODUCTION TO PROGRAMMING - TASK 15(Optional_task) =========
# ============   JOHNSON TEMILOLA - [18/03/2019] ===========================

# =================== PROGRAM DESCRIPTION ================================

# A program to check if a number inputted by the user is prime.
# A prime number is a positive integer greater than 1, whose only factors are 1 and the number itself.
# Examples of prime numbers are: 2, 3, 5, 7, etc.
# Ask the user to enter an integer.
# First check if the number is greater than 1.
# If it is greater than 1, check to see if it has any factors besides one and itself.
# i.e if there are any numbers between 2 and the number itself that can divide the number without any remainders 
# If the number is a prime number, print out the number and ' is a prime number!'
# If the number is not a prime number, print out the number and ' is not a prime number'

# ===========================================================================

# Python program to check if  
# given number is prime or not 
	
num = int(input("Please enter a number: ")) # Request a user to enter a number
 
# If given number is greater than 1 
if num >= 1: 
      
   # iterate from 2 to n / 2  
   for i in range(2, num//2): 
         
       # If num is divisible by any number between  
       # 2 and n / 2, it is not prime  
       if (num % i) == 0: 
           print(num, "is not a prime number") 
           break
   else: 
       print(num, "is a prime number") 
  
else: 
   print(num, "is not a prime number") 
