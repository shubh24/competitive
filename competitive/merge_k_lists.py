# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        arr = []
        counter = 0
        while counter < len(A):     
            length = A[counter]
            ll = []
            counter += 1
            for i in range(counter, counter + length):
                ll.append(A[i])
            counter += length
            arr.append(ll)

        pointers = [0 for p in range(len(arr))]

        res_ll = []
        end_pointer_state = [len(arr[i]) for i in range(len(arr))]
        
        while(pointers != end_pointer_state):
            min_ptr = 32768
    
            for i in range(len(arr)):
                try:
                    if arr[i][pointers[i]] < min_ptr:
                        min_ptr = arr[i][pointers[i]]
                        min_i = i
                except:
                    pass

            if pointers[min_i] != len(arr[min_i]):
                res_ll.append(arr[min_i][pointers[min_i]])
                pointers[min_i] += 1

        res_str = ""
        for r in range(len(res_ll)):
            if r != len(res_ll) - 1:
                res_str += str(res_ll[r]) + " --> "
            else:
                res_str += str(res_ll[r])

        print res_str 
# Solution().mergeKLists([10, 9, 8, 20, 38, 44, 55, 65, 66, 79, 87, 2, 68, 72, 5, 5, 55, 61, 73, 89, 2, 30, 73, 4, 28, 73, 84, 96, 3, 54, 82, 83, 5, 15, 33, 38, 94, 100, 1, 4, 5, 22, 32, 42, 64, 86, 2, 11, 78])