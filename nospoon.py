#tentative solution, needs major refactoring.
#first step will be to merge the two crawls (x and y)
#into a single subroutine.

import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

prints = [[]]

for i in range(height):
    line = input()  # width characters, each either 0 or .
    prints.append(list(line))
    print(line, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

prints.pop(0)
printer = [[]]
for i in range(width):
    for j in range(height):
        temp_prints = [i, j, -1, -1, -1, -1]
        if(j<height-1):
            t = []
            t.append([-1,-1])
            for k in range(j+1, height):
                if prints[k][i] != '.' and len(t) < 2:
                    t.insert(0, [k,i])
                
                if (i, k) == (2, 0):
                    print (k, i, prints[k][i], file=sys.stderr)
                #print (t, file=sys.stderr)
                    
            temp_prints[5], temp_prints[4] = t[0][0], t[0][1]
            
        if(i<width-1):
            t = []
            t.append([-1,-1])
            for k in range(i+1, width):
                if prints[j][k] != '.' and len(t) < 2:
                    t.insert(0, [j,k])
                #print (t, file=sys.stderr)

                    
            temp_prints[3], temp_prints[2] = t[0][0], t[0][1]
        
        temp_prints = [str(t) for t in temp_prints]
        if prints[j][i] != '.':
            printer.append(temp_prints)
        
        print (i, j, file=sys.stderr)
        
printer.pop(0)   
for temp in printer:
    print (temp, file=sys.stderr)
    print (' '.join(temp))

# Three coordinates: a node, its right neighbor, its bottom neighbor
#print("0 0 1 0 0 1")
