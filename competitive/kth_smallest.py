class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, k):
        ind = []
        for i in range(0, k):
            min_curr = 32768
            for j in range(0, len(A)):
                if j not in ind and A[j] < min_curr:
                    min_curr = A[j]
                    counter = j
            ind.append(counter)
        return min_curr
