# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:58:53 2021

@author: mitha
"""

while True:
    string=input()
    if string == '0':
        break
    new_string=''
    for i in range(len(string)-1,-1,-1):
        new_string+=string[i]
    if string==new_string:
        print("yes")
    else:
        print("no")
        