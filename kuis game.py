# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 00:02:59 2022

@author: asus
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 16:35:35 2022

@author: asus
"""
print("-----------------------------------")
print("selamat datang di kuis program saya")
print("-----------------------------------")
pemain = input("apakah kamu ingin bermain kuis ini??")

if pemain != " ya":
    quit()
print("oke mari kita mulai kuis ini")
score = 0
pernyataan = input ("apa kepanjangan dari PC? ")
if pernyataan == "personal computer":
    print("BENAR")
    score += 1
else:
    print("SALAH")
    
pernyataan = input ("apa kepanjangan dari VGA? ")
if pernyataan == "video graphic array" :
    print("BENAR")
    score += 1
else:
    print("SALAH")
    
pernyataan = input ("apa kepanjangan dari RAM? ")
if pernyataan == "random access memory" :
    print("BENAR")
    score += 1
else:
    print("SALAH")
    
pernyataan = input ("apa kepanjangan dari HDD? ")
if pernyataan == "hard disk drive" :
    print("BENAR")
    score += 1
else:
    print("SALAH")
pernyataan = input ("apa kepanjangan dari USB? ")
if pernyataan =="universal serial bus" :
    print("BENAR")
    score += 1
else:
    print("SALAH")
pernyataan = input ("apa kepanjangan dari SSD? ")
if pernyataan == "solid state drive":
    print("BENAR")
    score += 1
else:
    print("SALAH")
pernyataan = input ("apa kepanjangan dari LCD? ")
if pernyataan ==  "liquid crystal display" :
    print("BENAR")
    score += 1
else:
    print("SALAH")
    
print("anda punya " + str(score)+" pertanyaan yang benar!")
print("anda mempunyai nilai " + str(score/7 * 100)+"%.")