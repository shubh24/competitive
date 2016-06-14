class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def recurse_searchRange_left(self, A, B):
        low = 0
        high = len(A)
        mid = int((high+low)/2)
        if A[mid] > B:
            ans = self.recurse_searchRange_left(A[:mid], B)
        elif A[mid] < B:
            ans = mid + 1 + self.recurse_searchRange_left(A[mid+1:], B)
        elif A[mid] == B:
            ans = mid
        return ans

    def recurse_searchRange_right(self, A, B):
        low = 0
        high = len(A)
        mid = int((high+low)/2)
       
        if A[mid] < B:
            ans = mid + 1 + self.recurse_searchRange_right(A[mid+1:], B)
        elif A[mid] > B:
            ans = self.recurse_searchRange_right(A[:mid], B)
        elif A[mid] == B:
            ans = mid
        return ans


    def searchRange(self, A, B):
        if B not in A:
            return [-1,-1]
        ans = self.recurse_searchRange_left(A, B)
        if ans + 1 < len(A):
            high = ans + 1 + self.recurse_searchRange_right(A[ans+1:], B)
        else:
            high = ans
        # i = ans
        # while (i + 1 < len(A) and A[i+1] == B):
        #     i += 1
        # high = i
        # i = ans
        # while (i - 1> 0 and A[i-1] == B):
        #     i -= 1
        # low = i
        return [ans, high]

print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)