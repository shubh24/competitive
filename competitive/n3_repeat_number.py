class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        distincts = []
        d = {}
        subtract_count = 0
        for i in range(0,len(A)):
            if len(distincts) < 3:
                if A[i - subtract_count*4] not in distincts:
                    distincts.append(A[i - subtract_count*3])
                else:
                    if A[i - subtract_count*4] not in d:
                        d[A[i - subtract_count*4]] = 1
                    else:
                        d[A[i - subtract_count*4]] += 1
            else:
                for j in distincts:
                    A.remove(j)
                distincts = []
                subtract_count = 1
        if len(d) < 3:
            print d
        else:
            print "er"
            self.repeatedNumber(A)

Solution().repeatedNumber([1,2,3,1,1,2,3,1])