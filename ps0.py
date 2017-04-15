#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:19:58 2017

@author: katerynagargaun
"""

import math

string_x = input("Enter number x: ")
string_y = input("Enter number y: ")

integer_x = int(string_x)
integer_y = int(string_y)

integer_x_power_y = pow(integer_x, integer_y)
string_x_power_y = str(integer_x_power_y)
print("X**y = " + string_x_power_y)

integer_log_base = 2
integer_log_x = math.log(integer_x, integer_log_base)
string_log_x = str(integer_log_x)
print("log(x) = " + string_log_x)