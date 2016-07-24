class Solution:

    def recurse(self, A, B):
        if (A, B) in hash_map:
            return hash_map[(A, B)]
        if (B, A) in hash_map:
            return hash_map[(B, A)]

        elif len(A) == 0 and len(B) == 0:
            return 0
        elif len(A) != 0 and len(B) == 0:
            return len(A)
        elif len(A) == 0 and len(B) != 0:
            return len(B)
        if A[0] == B[0]:
            return self.recurse(A[1:], B[1:])
        else:
            min_local = min(1 + self.recurse(A, B[1:]), 1 + self.recurse(A[1:], B), 1 + self.recurse(A[1:], B[1:]))
            hash_map[(A, B)] = min_local
            return min_local            

    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        global hash_map 
        hash_map = {}
        res = self.recurse(A, B)
        return res
# print Solution().minDistance("bbaaaaaabbaabbabaaaa", "abbaababbaababbaaaba")
print Solution().minDistance("abaabbbbabaabaa", "aaaababa")
