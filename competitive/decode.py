class Solution:
    def __init__(self):
        self.hash = {}

    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if len(A) == 0:
            return 0
        count = 0
        if int(A) >= 1 and int(A) <= 26:
            count += 1
        if A[0] == "0":
            return 0

        elif len(A) == 1:
            if int(A) >= 1 and int(A) <= 9:
                return 1
        elif len(A) >= 2:
            if int(A[0]) >= 1 and int(A[0]) <= 9:
                if A[1:] not in self.hash:
                    ans = self.numDecodings(A[1:])
                    self.hash[A[1:]] = ans
                    count += ans
                else:
                    count += self.hash[A[1:]]

            if int(A[0:2]) >= 10 and int(A[0:2]) <= 26:
                if A[2:] not in self.hash:
                    ans = self.numDecodings(A[2:])
                    self.hash[A[2:]] = ans
                    count += ans
                else:
                    count += self.hash[A[2:]]
                
        # if count > 0:
        #     print count, A
        return count

# print Solution().numDecodings("2611055971756562")

