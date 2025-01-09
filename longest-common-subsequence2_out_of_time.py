class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res_dict = {}
        def get_sub_longest(txt1, txt2):
            original_txt1 = txt1
            original_txt2 = txt2
            key = original_txt1+"-"+original_txt2
            reverse_key = original_txt2+"-"+original_txt1
            if key in res_dict:
                return res_dict[key]
            if reverse_key in res_dict:
                return res_dict[reverse_key]


            set1 = set(txt1)
            set2 = set(txt2)
            common_set = set1 & set2
            txt1 = ''.join([x for x in txt1 if common_set])
            txt2 = ''.join([x for x in txt2 if common_set])
            print("txt1:", txt1)
            print("txt2:", txt2)
            print()


            count=0
            i = len(txt1)-1
            j = len(txt2)-1
            while(i>=0 and j>=0):
                if txt1[i]==txt2[j]:
                    i-=1
                    j-=1
                    count+=1
                else:
                    break

            txt1 = txt1[:i+1]
            txt2 = txt2[:j+1]

            if len(txt1)==0 or len(txt2)==0:
                return 0+count

            if len(txt1)==1 and len(txt2)==1:
                if txt1==txt2:
                    return 1+count
                else:
                    return 0+count

            i = len(txt1)-1
            cur1 = txt1[i]
            matched = False
            for j in range(len(txt2)-1, -1,-1):
                cur2 = txt2[j]
                if cur1==cur2:
                    matched = True
                    break

            if not matched:
                max_common = get_sub_longest(txt1[:i], txt2)
                res = max_common+count
                res_dict[key] = res
                res_dict[reverse_key] = res
                return max_common+count
            else:
                if j!=len(txt2)-1:
                    max_common1 = get_sub_longest(txt1[:i], txt2[:j])+1 # with cur1 and cur2
                    max_common2 = get_sub_longest(txt1[:i], txt2[:j]+txt2[j+1:])  # without cur1 and cur2
                    max_common3 = get_sub_longest(txt1[:i], txt2) # without cur1 only

                    res = max(max_common1, max_common2, max_common3)+count
                    res_dict[key] = res
                    res_dict[reverse_key] = res
                    return res
                else:
                    max_common1 = get_sub_longest(txt1[:i], txt2[:j])+1 # with cur1 and cur2

                    res = max_common1+count
                    res_dict[key] = res
                    res_dict[reverse_key] = res
                    return max_common1+count

        max_common = get_sub_longest(text1, text2)
        return max_common