class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
    	arr = []
    	p = 0
    	q = 0
    	while (p < len(A) or q < len(B)):
    		if q == len(B):
    			arr.append(A[p])
    			p += 1
    		elif p == len(A):
    			arr.append(B[q])
    			q += 1 
    		elif (A[p] <= B[q]):
    			arr.append(A[p])
    			p += 1
    		else:
    			arr.append(B[q])
    			q += 1

    	l = len(arr)
    	if l%2 == 0:
    		return (arr[int(l/2)] + arr[int(l/2) - 1])/float(2)
    	else:
    		return arr[int(l/2)]

print Solution().findMedianSortedArrays( [1 ,2, 4 ,5], [2 ,3])