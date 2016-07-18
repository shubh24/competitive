import operator
f = open("D-small-attempt0.in", "r")
g = open("clash.out", "w")
if __name__ == '__main__':
	test_cases = int(f.readline())
	for t in range(test_cases):
		coins_left, num_cards = f.readline().split(" ")
		coins_left = int(coins_left)
		max_levels = []
		curr_levels = []
		attack_levels = []
		coins_req = []

		for n in range(int(num_cards)):
			rl = f.readline().split(" ")
			max_levels.append(int(rl[0]))
			curr_levels.append(int(rl[1]))

			rl = f.readline().split(" ")
			for r in range(len(rl)):
				rl[r] = int(rl[r].strip("\n"))

			attack_levels.append(rl)

			rl = f.readline().split(" ")
			for r in range(len(rl)):
				rl[r] = int(rl[r].strip("\n"))

			coins_req.append(rl)

		while(coins_left > 0):
			loc_coins_req = 32768
			loc_attack_inc = 0
			flag = 0
			shortlist = {}

			for c in range(len(curr_levels)):
				if curr_levels[c] < max_levels[c]:
					this_attack_inc = attack_levels[c][curr_levels[c]] - attack_levels[c][curr_levels[c]-1]
					this_coins_req = coins_req[c][curr_levels[c]-1]

					if this_attack_inc >= loc_attack_inc and coins_left - this_coins_req >= 0:
						shortlist[c] = this_coins_req
						loc_attack_inc = this_attack_inc

			try:
				card_num = min(shortlist.iteritems(), key=operator.itemgetter(1))[0]
				loc_coins_req = coins_req[card_num][curr_levels[card_num]-1]
				flag = 1
			except:
				pass

			if flag == 1:
				curr_levels[card_num] += 1
				coins_left -= loc_coins_req
			else:
				break

		attack = 0
		for c in range(len(curr_levels)):
			attack += attack_levels[c][curr_levels[c]-1]

		g.write("Case #%s: %d"%(t+1, attack))
		g.write("\n")