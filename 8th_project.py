#!/usr/bin/python
# -*- coding: utf8 -*-

#Author Παναγιώτης Πράττης-Panagiotis Prattis Π15120
#This is the 8th exercise from the python exercise series for the class "ΕΙΣΑΓΩΓΗ ΣΤΗΝ ΕΠΙΣΤΗΜΗ ΤΩΝ ΥΠΟΛΟΓΙΣΤΩΝ - COMPUTER SCIENCE INTRODUCTION", University of Pireus
#Project's demands:
#Write a code which will read a file from a 8x8 table consisting of gaps (space) and 0. Then it displays the three rotations that it can have(by 90 degrees). Consider it like rotating a custom brick in Tetris.


import random

n=8;
table = [[random.choice([" ",0]) for i in range(n)] for j in range(n)];

#In case you don't want random spaces and zeroes use this code to create a table initialized with the numbers from 0 to 63
#n=8;
#table = [[i+j*n for i in range(n)] for j in range(n)];


print('this is the original table')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in table]))
print('------------------')

#Another way to print the table
#for i in range(0, 8, 1):
#        print table[i]




# zip(*table) will swap axes of 2d arrays by stacking corresponding items from lists
# into new lists. (The * operator tells the function to distribute the contained lists into arguments)
# The [::-1] statement reverses array elements




table2 = zip(*table[::-1])

print('this is the original table rotated by 90 degrees')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in table2]))
print('------------------')

table3 = zip(*table2[::-1])

print('this is the original table rotated by 180 degrees')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in table3]))
print('------------------')

table4 = zip(*table3[::-1])

print('this is the original table rotated by -90 degrees')
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in table4]))
print('------------------')
