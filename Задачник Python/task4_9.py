# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6uz_hnwdNZcd1tlAJnOVa_o0AtYl1Pi
"""

foot = 0.3048
km = 1000
a = float(input("Введите расстояние a (км): ")) * km
b = float(input("Введите расстояние b (фут): ")) * foot
if  a==b:
  print("Расстояния одинаковые!")
else:
  if a > b:
    print("Расстояние b меньше!")
  else:
    print("Расстояние a меньше!")

