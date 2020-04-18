#https://leetcode.com/problems/prime-arrangements/

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        count_primes = 0
        for i in range(2, n + 1):
            prime = True
            for k in range(2, int(math.sqrt(i)) + 1):
                if i % k == 0:
                    prime = False
            if prime:
                count_primes += 1
        return (self.factorial(count_primes) * self.factorial(n - count_primes)) % (10 ** 9 + 7)
        
    def factorial(self, n):
        if n <= 1:
            return 1
        else:
            fact = 1
            for i in range(2, n + 1):
                fact *= i
        return fact
            
