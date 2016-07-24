class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        rows = A[0]
        cols = A[1]

        arr = [[] for i in range(rows)]
        xs = []

        for i in range(rows):
            for j in range(cols):
                arr[i].append(A[2 + i*cols + j])
                if arr[i][j] == "X":
                    xs.append([(i,j)])
        
        change = 1
        while (change != 0):
            change = 0
            for x in xs:
                if x in xs:
                    for point_x in x: 
                        x_coord_x = point_x[0]
                        y_coord_x = point_x[1]
                        for y in xs:
                            if x != y and x in xs and y in xs:
                                for point_y in y:
                                    x_coord_y = point_y[0]
                                    y_coord_y = point_y[1]

                                    if abs(x_coord_x - x_coord_y)^abs(y_coord_x - y_coord_y) == 1:
                                        for i in x:
                                            y.append(i)
                                        print x, xs
                                        xs.remove(x)
                                        change = 1
                                        print xs
            
        return len(xs)

print Solution().black([2,3,"X","X","X", "X", "O", "X"])