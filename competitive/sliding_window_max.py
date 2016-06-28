class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        q = [A[0]]
        arr = []
        ptr = B-1

        for i in range(min(len(A)-1,1), len(A), 1):
            if ptr <= len(A)-1:
                if len(q) > 0:
                    m = q[0]
                    if A[i] > m:
                        m = A[i]
                        q = [m]*B
                    else:
                        q.append(A[i])    
                else:
                    m = A[i]
                    q = [m]
                ans = q[0]   
                q.remove(ans)
                arr.append(ans)
                ptr += 1
            else:
                break
        if B == 1 and len(A) != 1 and len(q) > 0:
            arr.append(q[0])
        return arr

print Solution().slidingMaximum( [ 105, 420, 569, 534, 912, 145, 566, 462, 51, 34, 671, 487, 627, 475, 647, 221, 145, 966, 612, 685, 786, 982, 834, 433, 979, 158, 221, 641, 435, 631, 664, 10, 815, 86, 338, 822, 450, 747, 598, 599, 6, 652, 829, 547, 604, 699, 44, 141, 427, 957, 221, 816, 952, 716, 337, 950, 889, 510, 492, 550, 726, 396, 218, 939, 220, 923, 380, 197, 209, 52, 194, 753, 539, 465, 987, 975, 731, 776, 385, 209, 969, 993, 518, 237, 47, 130 ], 1)