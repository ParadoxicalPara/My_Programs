"""Author: ParadoxicaL"""
"""  Longest common substring program """
def longestSubStr(strings):
    strs = strings.split(",")
    str1, words = strs[0], strs[1:]
    subStrs = [""]
    subStr = ""
    longestLen = 0
    for ch in str1:
        if len(list(filter(lambda wrd: subStr+ch in wrd, strs)))==len(strs):
            subStr+=ch
            if len(subStr)>longestLen:
                longestLen = len(subStr)
                subStrs = [subStr]
            elif len(subStr)==longestLen:
                subStrs.append(subStr)
        elif len(list(filter(lambda wrd: ch in wrd, strs)))==len(strs):
            subStr = ch
        else:
            subStr = ""
    if len(subStrs)!=1:
        return subStrs
    else:
        return subStrs[0]

