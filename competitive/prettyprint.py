class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        arr = []
        for i in range(0, A):
            new_arr = []
            c = A
            flag = 0
            for j in range(0, 2*A - 1):
                new_arr.append(c)
                if i == 2*A-j-2:
                    flag = 1
                if flag == 0 and c > A-i:
                    c -= 1
                if flag == 1:
                    c+= 1
            arr.append(new_arr)
        for i in range(len(arr)-2, -1, -1):
            arr.append(arr[i])
        return arr