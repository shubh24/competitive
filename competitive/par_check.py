class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):

        arr = []
        curr = 0 
        for i in range(len(A)):
            var = A[i]
            if var == "(":
                arr.append(var)
                curr += 1

            elif var == ")":
                if curr > 0 and arr[curr-1] == "(" :
                    del arr[curr-1]
                    curr -= 1
                else:
                    return 0

            if var == "{":
                arr.append(var)
                curr += 1

            elif var == "}":
                if curr > 0 and arr[curr-1] == "{":
                    del arr[curr-1]
                    curr -= 1
                else:
                    return 0

            if var == "[":
                arr.append(var)
                curr += 1

            elif var == "]":
                if curr > 0 and arr[curr-1] == "[":
                    del arr[curr-1]
                    curr -= 1
                else:
                    return 0


        if len(arr) == 0:
            return 1
        else:
            return 0

print Solution().isValid("()[]{}(")