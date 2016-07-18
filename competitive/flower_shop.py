import numpy as np
import operator
f = open("C-large.in", "r")
g = open("flower_large.out", "w")
if __name__ == '__main__':
	test_cases = int(f.readline())
	res = []
	for t in range(test_cases):
		months = int(f.readline())
		money_line = f.readline().split(' ')
		coeffs = []
		for money in money_line:
			coeffs.append(int(money.strip("\n")))
		coeffs[0] = -1*coeffs[0]
		roots = np.roots(coeffs)
		imag_dic = {}
		for r in range(len(roots)):
				roots[r] = roots[r] - 1
				if roots[r].real < 1 and roots[r].real > -1:
					imag_dic[roots[r].real] = abs(roots[r].imag - 0)
		res.append(min(imag_dic.iteritems(), key=operator.itemgetter(1))[0])

	for r in range(len(res)):
		g.write("Case #%s: %s"%(r+1, res[r]))
		g.write("\n")
