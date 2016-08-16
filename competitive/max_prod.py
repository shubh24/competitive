class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        m = -1
        for i in range(len(A)):
            p = A[i]
            if p > m:
                m = p
            for j in range(i+1, len(A)):
                a = A[i+1:j]
                for k in a:
                    p *= k
                if p > m:
                    m = p

        return m

# print Solution().maxProduct([0])