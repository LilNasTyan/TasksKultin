# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n6uz_hnwdNZcd1tlAJnOVa_o0AtYl1Pi
"""

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if  a==b:
  print("Первое и второе числа равны")
if a > b:
  maximum = a
  minimum = b
else:
  maximum = b
  minimum = a
print("max{{{}, {}}} = {}".format(a, b, maximum))
print("min{{{}, {}}} = {}".format(a, b, minimum))

