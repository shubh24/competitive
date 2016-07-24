class Solution:


    def recurse(self, first, second):
        if len(first) > 2:
            selected = []
            max_local_total = -1

            for i in range(2):
                result, local_total = self.recurse(first[2:], second[2:])
                if first[i] + local_total > max_local_total:
                    max_local_total = first[i] + local_total
                    selected = [first[i]] + result

                result, local_total = self.recurse(first[2:], second[2:])
                if second[i] + local_total > max_local_total:
                    max_local_total = second[i] + local_total
                    selected = [second[i]] + result

            return selected, max_local_total

        elif len(first) == 1:
            max_num = max(first[0], second[0])
            return [max_num], max_num

        elif len(first) == 2:
            max_num  = max(first[0], second[0], first[1], second[1])
            return [max_num], max_num 

    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        cols = A[1]

        first = A[2:2+cols]
        second = A[2+cols:]

        a, b = self.recurse(first, second)

        print a, b
Solution().adjacent([2,4, 1, 2, 3, 4,2  , 3, 4, 5])