# https://leetcode.com/problems/count-primes/
# Count the number of prime numbers less than a non-negative number, n.
def countPrimes(self, n):
    if n <= 2 : return 0
    res = 1
    trueTable = [True]*n
    trueTable[0:2] = [False]*2

    for i in range(2,int(n ** 0.5) + 1) :
        if trueTable[i] == True :
            trueTable[i*2:n:i] = [False]*((n - 1 - i*2)/i + 1)
    return sum(trueTable)
