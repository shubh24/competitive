class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def numRange(self, A, B, C):
    	count = 0
    	for i in range(0,len(A)):
    		for j in range(i+1, len(A)+1):
    			loc_sum = sum(A[i:j])
    			if loc_sum >= B and loc_sum <= C:
    				count += 1
    	return count 

print Solution().numRange([10, 5, 1, 0, 2], 6, 8)