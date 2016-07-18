class Solution:
    # @param A : string
    # @return a list of strings
    mapping = {"0":{"0"}, "1":{"1"}, "2":{"a","b","c"}, "3":{"d","e","f"}, "4":{"g","h","i"}, "5":{"j","k","l"}, "6":{"m","n","o"},"7":{"p","q","r","s"},"8":{"t","u","v"},"9":{"w","x","y","z"}}

    def func(self, A):

        if len(A) == 1:
            return list(self.mapping[A[0]])

        results = []
        mapped_letters = self.mapping[A[0]]
    
        for letter in mapped_letters:
                recursed_return = self.func(A[1:])
                for r in recursed_return:
                    results.append(letter + r)

        return results

    def letterCombinations(self, A):
        val = A.split()[-1]
        results = self.func(val)
        return sorted(results)

Solution().letterCombinations("Letter Digit 2")             