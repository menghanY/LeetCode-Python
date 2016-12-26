class Solution(object):
    #dfs超时
    def __init__(self):
        self.nums = 0
    def uniquePaths1(self, m, n):

        def dfs(x,y,m,n):
            if x == m and y == n :
                self.nums += 1
            else:
                if x < m : dfs(x+1,y,m,n)
                if y < n : dfs(x,y+1,m,n)

        dfs(1,1,m,n)
        return self.nums
    #https://discuss.leetcode.com/topic/72457/39ms-python-dp
    def uniquePaths2(self, m, n):
        table = [[0 for  x in range(n)] for x in range(m)]
        table[0][0] = 1
        for i in range(m) :
            for j in range(n) :
                if  table[i][j] == 0 :
                    table[i][j] = (0 if i == 0 else table[i-1][j]) + (0 if j == 0 else table[i][j-1])
                print(table[i][j])
        return table[m - 1][n - 1]

s = Solution()
print(s.uniquePaths1(3,7))
print(s.uniquePaths2(3,7))