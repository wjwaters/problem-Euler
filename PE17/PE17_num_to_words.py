# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 13:05:51 2017

@author: wjwaters
"""

"PE#17-NUMBERS TO WORDS"

def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000


    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + 'hundred'
        else: return d[num // 100] + 'hundredand' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + 'thousand'
        else: return int_to_en(num // k) + 'thousand' + int_to_en(num % k)


    raise AssertionError('num is too large: %s' % str(num))
   
    
char=''
for i in range(1,1001):
    char+=int_to_en(i)
    
N=len(char)
print("The sum of characters of all numbers from 1 to 1000 is "+str(N))