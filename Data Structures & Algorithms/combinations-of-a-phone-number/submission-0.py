class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numAlphListFreq = {2:["a", "b", "c"], 3:["d", "e", "f"], 
                           4:["g", "h", "i"], 5:["j", "k", "l"], 
                           6:["m", "n", "o"], 7:["p", "q", "r", "s"], 
                           8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
        res, sol = [], []

        def backtrack(i):
            if digits == "":
                return []
            if len(sol) == len(digits):
                res.append(''.join(sol))
                return
            if i >= len(digits) or digits[i] == 0 or digits[i] == 1:
                return
            
            digit = digits[i]
            digiVal = int(digit)
            cur = numAlphListFreq[digiVal]
            print(cur)

            for x in cur:
                sol.append(x)
                backtrack(i + 1)
                sol.pop()
        backtrack(0)
        return res