#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 21:42:28 2021

@author: sercan
"""

liste = ["Elma",35,"Merhaba",3.14,5]

print(liste)

print(len(liste))

print(liste[2])

print(liste[:4])

print(liste[::2])

print(liste[1:4:2])

print(liste[::-1 ])


liste1 = [1,2,3]

liste2 = [4,5,6]

liste3 = liste1 + liste2

print(liste3)

print(liste1 * 3) #anlık değişim

liste1 = liste1 * 3

print(liste1)

liste2[:2] = [10,11]

print(liste2)

print(liste)
liste.append("sercan")

print(liste)

liste.pop()
print(liste)

liste.pop(0)

print(liste)

abc = [23,5,78,3,56]

abc.sort()
print(abc.sort(reverse = True))

abcd = ["sercan","asfasf","plaş","sad"]
print(abcd.sort())
print(abcd.sort(reverse = True))
