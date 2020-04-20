#!/usr/bin/python3.8
 
import math

# Copied from https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
def primes(until):
    primes = []
    for num in range(3,until+1,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            primes.append(num)
    return primes

print("Content-type: text/html")
print("\n")
print("<html>")
until = 100
print("<h1>Prime Numbers until " + until + "</h1>")
for number in primes(until):
    print('<span style="border: 1px solid red; padding: 5px; margin: 5px">')
    print(number)
    print('</span>')
print("</html>")
