#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:21:52 2018

@author: zhaojun
"""

rows = 'ABCDEFGHI'
cols = '123456789'
def cross(a, b):
      return [s+t for s in a for t in b]
diag_units = [r+c for r,c in zip(rows,cols)]
diag_units2 = [r+c for r,c in zip(rows, cols[::-1])]