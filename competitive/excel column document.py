class Solution:
    # @param A : string
    # @return an integer
    def getCorrespondingNumber(self, x):
        return ord(x) - 64

    def titleToNumber(self, A):
        length = len(A)

        c = 0
        arr = []
        for i in range(0, length):
            arr.append(self.getCorrespondingNumber(A[i]))
        for i in range(length, 0, -1):
            c += pow(26, length - i)*arr[i - 1]
        return c

if __name__ == '__main__':
     print Solution().titleToNumber("D")