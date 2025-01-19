class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res_dict = {}
        if len(text1)<=0 or len(text2)<=0:
            return 0
        
        if text1[0]==text2[0]:
            res_dict["0-0"] = 1
        else: 
            res_dict["0-0"] = 0

        def get_sub_longest(i, j):
            key = str(i) + "-" + str(j)
            if key in res_dict:
                return res_dict[k]

            ....Seems not working....


        max_common = get_sub_longest(text1, text2)
        return max_common

