class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        memo[0] = 1
        memo[1] = 1
        def dp(n, memo):
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n-1, memo) + dp(n-2, memo)

            return memo[n]
        return dp(n, memo)