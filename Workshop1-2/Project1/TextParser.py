#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:59:28 2020

@author: Muhammad
"""

# Parsing a text file for numerical data

covid = open('COVID.txt')

word_list = covid.read().split()

numbers = [int(x) for x in word_list if x.isdigit()]
#numbers.sort()

print(numbers)
covid.close()