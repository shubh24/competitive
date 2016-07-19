class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        max_count = -1
        for i in range(0, len(A)):
            for j in range(i, len(A)):
                min_x = A[i]
                min_y = B[i]
                max_x = A[j]
                max_y = B[j]


                if min_x == max_x:
                    count = abs(max_y - min_y) + 1

                else:
                    slope = (max_y - min_y)/(max_x - min_x)
                    c = max_y - (slope*max_x)

                    count = 2
                    
                    for i in range(min(min_x, max_x) + 1, max(min_x, max_x)):
                        y = slope*i + c
                        if y - int(y) == 0:
                            count += 1

                if count > max_count:
                    max_count = count
        return max_count

print Solution().maxPoints([1, 1, 1], [0, 4, -1])
