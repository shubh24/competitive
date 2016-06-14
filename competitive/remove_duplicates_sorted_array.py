class Solution:
	def removeDuplicates(self, A):
		for i in range(len(A)):
			for j in range(len(A)-1, i, -1):
				if A[j] == A[i]:
					del A[j]
		return len(A)

print Solution().removeDuplicates([0])