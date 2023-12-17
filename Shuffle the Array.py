"""
https://leetcode.com/problems/shuffle-the-array

問題文：
形式の 要素で構成される配列 nums があるとします。2n[x1,x2,...,xn,y1,y2,...,yn]
配列を の形式で返します。[x1,y1,x2,y2,...,xn,yn]

例 1:

入力: nums = [2,5,1,3,4,7]、n = 3
出力: [2,3,5,4,1,7] 
説明: x1=2 であるため、x< a i=8>2=5、x3=1、y 1=3、y2=4、y3=7 の場合、答えは [2,3,5,4,1,7] となります。


この問題は、与えられた配列 nums を特定のパターンに従って並べる問題で、
配列 nums は 2n 個の要素を持っており、この配列を [x1, y1, x2, y2, ..., xn, yn] の形に並べればOK
"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            x = nums[i]
            y = nums[i + n]
            result.append(x)
            result.append(y)
        return result