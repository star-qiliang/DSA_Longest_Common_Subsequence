class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        set2 = set(text2)
        common_set = set1 & set2
        text1 = [x for x in text1 if x in common_set]
        text2 = [x for x in text2 if x in common_set]
        text1 = ''.join(text1)
        text2 = ''.join(text2)

        print("text1:", text1)
        print("text2:", text2)

        len_text1 = len(text1)
        len_text2 = len(text2)

        max_len = 0
        base1 = ""
        for i in range(len_text1):
            for j in range(len_text2):
                k = 0
                base2 = ""
                cur_max = 0
                while i+k<len_text1 and j+k<len_text2:
                    print("i:", i)
                    print("j:", j)
                    print("cur_max:", cur_max)
                    print()
                    base1 = base1 + text1[i+k]
                    base2 = base2 + text2[j+k]

                    if base1==base2:
                        cur_max+=1
                        if cur_max>max_len:
                            max_len = cur_max
                    else:
                        base1 = ""
                        base2 = ""
                    
                    k+=1
                
        return max_len