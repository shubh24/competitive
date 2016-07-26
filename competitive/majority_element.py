class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
    	dict = {}
    	for i in A:
    		if i not in dict:
    			dict[i] = 1
    		else:
    			dict[i] += 1

    	return max(dict.iteritems(), key=lambda x:x[1])[0]

print Solution().majorityElement([2,3,2])
