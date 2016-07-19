class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
		lines = A.split()
		size = int(lines[0].split(",")[0])
		lines = lines[1:]

		cols = []
		boxes = []

		for line in lines:
			check = [0 for i in range(0,size)]
			for elem in line:
				if elem in ("1","2","3","4","5","6","7","8","9"):
					if check[int(elem) - 1] > 0:
						return 0
					else:
						check[int(elem) - 1] = 1

		for i in range(0, size):
			check = [0 for i in range(0,size)]
			for line in lines:
				elem = line[i]
				if elem in ("1","2","3","4","5","6","7","8","9"):
					if check[int(elem) - 1] > 1:
						return 0
					else:
						check[int(elem) - 1] = 1								

		for i in range(0, size):
			check = [0 for x in range(0,size)]
			root = int(pow(size, 0.5))
			for j in range(i - i%root, i - i%root + root):
				for k in range((i%root)*root, (i%root)*root + root):
					elem = lines[j][k] 
					if elem in ("1","2","3","4","5","6","7","8","9"):
						if check[int(elem) - 1] > 0:
							return 0
						else:
							check[int(elem) - 1] = 1

		return 1

print Solution().isValidSudoku("9 ....5..1. .4.3..... .....3..1 8......2. ..2.7.... .15...... .....2... .2.9..... ..4......")
