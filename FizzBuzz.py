class Solution(object):
    def fizzBuzz(self, n):
        if n == 0 : return ["FizzBuzz"]
        l = []
        for x in range(1,int(n + 1)):
            myStr = ""
            if x % 3 == 0 :
                myStr += "Fizz"
            if x % 5 == 0 :
                myStr += "Buzz"
            if len(myStr) == 0 :
                myStr += str(x)
            l.append(myStr)
        return l

a = Solution()
print(a.fizzBuzz(15))






