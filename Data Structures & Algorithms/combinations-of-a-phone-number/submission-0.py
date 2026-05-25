class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        mapp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        for digit in digits:
            tmp = []
            for perm in res:
                for letter in mapp[digit]:
                    tmp.append(perm+letter)
                    print(tmp)
            res = tmp
            print("doing res=tmp")

        return res



        