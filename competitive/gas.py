class Solution:
    # @param gas : tuple of integers
    # @param cost : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):

    	num_stations = len(gas)

    	for start in range(num_stations):
	    	gas_in_tank = 0
	    	flag = 0
    		
    		if flag == 1:
    			return 1

    		for i in range(start, start + num_stations):
    			gas_in_tank += gas[i%num_stations]

    			if gas_in_tank < cost[i%num_stations]:
    				flag = -1
    				break
    			else:
	    			gas_in_tank -= cost[i%num_stations]

    		if i == (start + num_stations - 1) and flag != -1:
    			flag = 1
    			min_start = start
    			break

    	if flag == 1:
    		return min_start
    	else:
    		return -1

print Solution().canCompleteCircuit([1,0], [1,0])
