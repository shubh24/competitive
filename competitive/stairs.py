class Solution:
    def recurse(self, A):
        val = 0
        if A == 1 or A == 0:
            self.memo[A] = 1
            return 1
        elif A < 0:
            return 0
        if A not in self.memo:
            val += self.recurse(A-2)
            val += self.recurse(A-1)
            self.memo[A] = val

        return self.memo[A]



    # @param A : integer
    # @return an integer

    def climbStairs(self, A):
        self.memo = {}
        return self.recurse(A)

# Solution().climbStairs(5)