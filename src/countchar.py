# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:35:19 2017

@author: AutuanLiu
"""

def countchar(str):
# 保存结果
    ret = [0] * 26
    for ch in str:
        if ord(ch) - 97 < 0 or ord(ch) - 97 > 25:
            continue
        else:
            ret[ord(ch) - 97] += 1
    return ret

if __name__ == "__main__":
    str = input()
    str = str.lower()
    print(countchar(str))