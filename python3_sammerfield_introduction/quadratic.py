#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import cmath
import math
import sys
quad = "\N{SUPERSCRIPT TWO}"
arrow = "\N{RIGHTWARDS ARROW}"

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x


print("ax{0} + bx + c = 0".format(quad))
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else: # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
if b == 0 and c != 0:
    equation = ("{0}x{4} {2:+} = 0 "
            "{5} x = {3}").format(a, b, c, x1, quad, arrow)
elif c == 0 and b != 0:
    equation = ("{0}x{4} {1:+}x = 0 "
            "{5} x = {3}").format(a, b, c, x1, quad, arrow)
elif (b and c) == 0:
    equation = ("{0}x{4}= 0 "
            "{5} x = {3}").format(a, b, c, x1, quad, arrow)
else:
    equation = ("{0}x{4} {1:+}x {2:+} = 0 "
            "{5} x = {3}").format(a, b, c, x1, quad, arrow)
if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)
