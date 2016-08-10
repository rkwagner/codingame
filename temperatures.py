import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526


if len(temps) == 0:
    print ( 0 )
else:
    tempe = temps.split(' ')
    temp_abs = 5527
    for i in range(len(tempe)):
        if abs(int(tempe[i])) < abs(temp_abs):
            temp_abs = int(tempe[i])
        elif int(tempe[i]) == abs(temp_abs):
            temp_abs = int(tempe[i])
    print( temp_abs )
    print( tempe, file=sys.stderr )

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#print("result")
