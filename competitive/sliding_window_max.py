class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):

        res = []
        arr = A[:B]
        max_num = max(arr)
        if len(A) > 1:
            res.append(max(A[0], A[1]))
        else:
            res.append(A[0])
            return res

        if B > len(A):
            return [max(A)]

        for start in range(1, len(A) - B +1):
            #arr = A[start:start+B]
            if arr[0] != max_num:
                del arr[0]

                arr.append(A[start+B-1])
                if A[start+B-1] > max_num:
                    max_num = A[start+B-1]
                else:
                    pass    
            if arr[0] == max_num:
                del arr[0]
                max_num = -1
                arr.append(A[start+B-1])
                max_num = max(arr)

            res.append(max_num)

        return res

print Solution().slidingMaximum( [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ],2)