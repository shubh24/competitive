import collections
def flip(A):
	flag = 0
	for i in A:
		if i == "0":
			flag = 1
			break
	if flag == 1:
		dict = {}
		for i in range(len(A)):
			zero_count = 0
			one_count = 0
			local_dict = {}
			for j in range(i, len(A), 1):
				if A[j] == '0':
					zero_count += 1
				elif A[j] == '1':
					one_count += 1		
				local_dict[int(j)] = zero_count - one_count

			max_k = -1
			max_local_dict = -32768
			bro = sorted(local_dict)
			for k in bro:
				if local_dict[k] > max_local_dict:
					max_local_dict = local_dict[k]
					max_k = k
			dict[(i,max_k)] = max_local_dict 
		yo = sorted(dict)
		val = -32768
		max_j = -1
		for j in yo:
			if dict[j] > val:
				max_j = j
				val = dict[j]


		return [max_j[0]+1, max_j[1]+1]
	else:
		return []

print flip( "01010101010101010111100101010101010101")