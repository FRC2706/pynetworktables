#!/usr/bin/env python3

import sys

parms = input("Enter command color: ")
command=parms.split()[0]
color=parms.split()[1]

print("Command: %s" % command)
print("Color:   %s" % color)
