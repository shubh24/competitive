class Solution:
	def dist(self, a,b):
		x_dist = abs(int(a[0])-int(b[0]))
		y_dist = abs(int(a[1])-int(b[1]))
		diags = min(x_dist,y_dist)

		return diags + abs(x_dist - y_dist)

	def coverPoints(self, X, Y):
		arr = []
		for j in range(len(X)):
			arr.append((X[j], Y[j]))
		curr = arr[0]
		counter = 0
		for i in range(1, len(arr), 1):
			next = arr[i]
			counter += self.dist(curr, next)
			curr = next

		return counter
