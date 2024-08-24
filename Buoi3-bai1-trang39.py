# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:09:47 2024

@author: pc
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
chuoitach = chuoi.split(", ")
print("1. Tách thành các sub-string:")
print("\n".join(chuoitach))
print("\n2.Tách thành các sub-string:")
print(chuoitach[0])
print(chuoitach[1])
print(chuoitach[2].replace("P. ",""))
print(chuoitach[3].replace("Q. ",""))
print(chuoitach[4].replace("Tp. ",""))