# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:44:26 2021

@author: mitha
"""
def gcd(a,b):
    if b>a:#a를 가장 큰 수로 할 필요가 있음
        temp=b
        b=a
        a=temp
        
    while b!=0:
        n=a%b
        a=b
        b=n
    return a

a,b=map(int,input().split())
result=gcd(a,b)
print(result)
print(int(a*b/result))
