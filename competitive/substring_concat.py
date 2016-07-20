import itertools
class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if len(A) < len(B)*len(B[0]):
            return []
        perms = itertools.permutations(B)
        results = []
        c = 0
        for p in perms:
            res = ""
            for i in p:
                res += i

            indexes = [n for n in xrange(len(A)) if A.find(res, n) == n]
            for index in indexes:
                if index < len(A) and index >= 0:
                    results.append(index)

        return list(set(results))

print Solution().findSubstring("acaaacbcbccbaabaccabcbbcaaccbbbbcbabaacbbcbccababb",["cabccbbbc", "abbccabbc" ,"bbbcbbbaa" ,"acbaabcab" ,"ccacabccb" ,"bbacaabca", "acacbaacb" ,"aabbcccab" ,"ccccbbcaa" ,"baaccaabc"])