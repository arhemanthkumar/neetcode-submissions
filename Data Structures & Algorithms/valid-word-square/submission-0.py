class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        flag = True
        lhs = ""
        rhs = ""

        for i in range(len(words)):

            lhs = words[i]
            len_of_lhs = len(lhs)

            for j in range(len_of_lhs):
                rhs = rhs + words[j][i]

            if lhs != rhs:
                flag = False

            rhs = ""

        return flag
