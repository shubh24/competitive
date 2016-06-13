class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    counter = 0
    arr = {}

    def recurse_uniquePaths(self, A, B):
        if A == 1 or B == 1:
            self.counter += 1
        else:
            if (A, B) not in self.arr:
                c = self.counter
                #right
                if B > 1:
                    self.recurse_uniquePaths(A, B - 1)
                #down
                if A > 1:
                    self.recurse_uniquePaths(A - 1, B)

                self.arr[(A, B)] = self.counter - c
                self.arr[(B, A)] = self.counter - c     
            else:
                self.counter += self.arr[(A, B)]

    def uniquePaths(self, A, B):
        self.recurse_uniquePaths(A, B)
        return self.counter

if __name__ == '__main__':
    print Solution().uniquePaths(14, 15)