class Solution:
	def removeDuplicates(self, A):
		for i in range(len(A)-1):
			while (i+1 < len(A) and A[i+1] == A[i]):
				del A[i+1]
		print A
		return len(A)

print Solution().removeDuplicates([0,1,1,1])