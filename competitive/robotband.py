import itertools

if __name__ == '__main__':
	test_cases = int(raw_input())

	all_ints = []
	for i in range(test_cases):
		count = 0
		n, k = raw_input().split()
		arr = []

		for j in range(4):
			inp = raw_input().split()
			for yo in range(len(inp)):
				inp[yo] = int(inp[yo])
				all_ints.append(inp[yo])
			arr.append(inp)



		serials = list(itertools.permutations(all_ints, 4))			
		ans = []

		for s in serials:
			flag = 0
			for num in range(0,4):
				if s[num] not in arr[num]:
					flag = 1
					break
			if flag == 0:
				res = 0
				for num in range(0,4):
					res = res^s[num]
					if res == int(k):
						if s not in ans:
							ans.append(s)

		for var in ans:
			prod = 1
			for v in range(0,4):
				prod *= arr[v].count(var[v])
			count += prod

		print "Case #%d: %d"%(i+1, count) 