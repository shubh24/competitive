class Solution:
    # @param A : list of list of chars

    def shortlist(self, i, j, arr):
        flag = 0
        for j_check in range(0, j):
            if arr[i][j_check] == "X":
                flag = 1

        if flag == 1:
            for j_check in range(j + 1, len(arr[0])):
                if arr[i][j_check] == "X":
                    flag = 2


        if flag == 2:
            for i_check in range(0, i):
                if arr[i_check][j] == "X":
                    flag = 3

        if flag == 3:
            for i_check in range(i + 1, len(arr)):
                if arr[i_check][j] == "X":
                    flag = 4

        if flag == 4:
            return True
        else:
            return False


    def solve(self, A):

        length = len(A)
        rows = int(pow(length, 0.5))
        cols = rows

        arr = [[] for i in range(rows)]
        shortlist = []
        for i in range(rows):
            for j in range(cols):
                arr[i].append(A[i*cols + j])

        
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == "O":
                    if self.shortlist(i, j, arr):
                        shortlist.append((i, j))  

        for i in shortlist:
            arr[i[0]][i[1]] = "X"

        res = ""
        for i in range(rows):
            string = ""
            for j in range(cols):
                string += arr[i][j]
            res += string + " "
        return res

# print Solution().solve(["X","X","X","X","O","X","X","X","X"])      
print Solution().solve([ "O" ])