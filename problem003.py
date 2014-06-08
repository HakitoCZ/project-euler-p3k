#!/usr/bin/python3
'''
Problem: http://projecteuler.net/problem=3
Description:
  The prime factors of 13195 are 5, 7, 13 and 29.
  What is the largest prime factor of the number 600851475143 ?

WARNING:
  !! this solution is extremely unefficient !!

Process description:
  Script is looking for prime numbers in range 2 to 600851475143. If selected number is not prime, that means is devidable without leftover, it skips to next number. If number is prime, script set it as value of variable 'q' and when it reaches the number 600851475143, it prints the variable 'q'.
  It works but you'd need processor from NASA cooled with liquid nitrogen to work in bearable speed.
  It is probably the most unefficient solution but it's the best I can think of for the week I'm trying to solve it.
'''

q = 0
for n in range(2,600851475143):
  for x in range(2,n):
    if n % x == 0:
      break
  else:
    q = n

print(q)
