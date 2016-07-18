class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def func(self, A):

        if len(A) == 1:
            return [[A[0]]]

        res = []        
        for i in range(len(A)):
            recurse_res = self.func(A[:i] + A[i+1:])
            for r in recurse_res:
                res.append([A[i]] + r)
        return res

    def permute(self, A):
        result = self.func(A)
        return result

Solution().permute([1,2,3,4,0])
