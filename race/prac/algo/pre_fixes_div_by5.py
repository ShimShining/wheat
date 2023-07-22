class Solution:
    def prefixesDivBy5(self, A):
        X = 0
        bool_list = []
        for i in range(len(A)):
            if (2 * X + A[i]) % 5 == 0:
                bool_list.append("true")
            else:
                bool_list.append("false")
            X = 2 * X + A[i]
        return bool_list

if __name__ == "__main__":
    A = [0,1,1]
    pref = Solution()
    res = pref.prefixesDivBy5(A)
    print(res)
