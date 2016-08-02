class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
    	self.arr = {}

    def process(self, nums):
    	
    	if len(nums) == 1 or len(nums) == 0:
    		return 1
    	
    	sum = 0
    	for i in range(len(nums)):
    		remaining_arr = nums[:i] + nums[i+1:]
    		lt = []
    		gt = []
    		for j in range(len(remaining_arr)):
    			if remaining_arr[j] <= nums[i]:
    				lt.append(remaining_arr[j])
    				lt = sorted(lt)
    			else:
    				gt.append(remaining_arr[j])
    				gt = sorted(gt)

    		if tuple(lt) not in self.arr:
	    		res_lt = self.process(lt)
    			self.arr[tuple(lt)] = res_lt
    		else:
    			res_lt = self.arr[tuple(lt)]

    		if tuple(gt) not in self.arr:
	    		res_gt = self.process(gt)
    			self.arr[tuple(gt)] = res_gt
    		else:
    			res_gt = self.arr[tuple(gt)]

    		sum += res_lt*res_gt

    	return sum

    def numTrees(self, A):
    	nums = [i for i in range(A)]
    	return self.process(nums)

print Solution().numTrees(3)