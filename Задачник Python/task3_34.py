# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6uz_hnwdNZcd1tlAJnOVa_o0AtYl1Pi
"""

n=input("Введите результат преобразований трехзначного числа: ")
if int(n)==0 or int(n)>999:
   print("Результат не соответствует условиям задачи!")
else:
  if int(n) < 10:
    x = int(n)*100
    print("Задуманное число равно: ", x)
  else:
      if int(n) < 100:
        x = int(n) // 10 + (int(n) % 10)*100
        print("Задуманное число равно: ", x)
      else:
        if len(n)==3:
          x = int(n[len(n)-1]+n[:len(n)-1])
          print("Задуманное трехзначное число равно: ", x)

