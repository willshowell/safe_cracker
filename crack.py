# crack.py 
#
# each 'row' is listed as an array. some are physically linked. a -1 
# means that nothing exists in that space.
#
# r0:  outer row
# r1:  next most outer row - physically connected to r0
# r1s: can overlap r1 and is slotted
# r2:  inside the r1 row but is connected to r1s
# ...
# r3s: inner most row is slotted and not attached to anythin
#
# trying to get a sum of 40 for each column
#

from collections import deque

attempts = 1

# r0 and r1 are linked together just like this
r0  = [10,  2, 15, 23, 19,  3,  2,  3, 27, 20, 11, 27, 10, 19, 10, 13]#
r1  = [ 9, 22,  9,  5, 10,  5,  1, 24,  2, 10,  9,  7,  3, 12, 24, 10]#

# r1s and r2 are linked together just like this
r1s = [ 9, -1, 16, -1, 17, -1,  2, -1,  2, -1, 10, -1, 15, -1,  6, -1]#
r2  = [ 1,  1, 11, 27, 14,  5,  5,  7,  8, 24,  8,  3,  6, 15, 22,  6]#

# r2s and r3 are linked together just like this
r2s = [14, -1,  5, -1, 10, -1,  2, -1, 22, -1,  2, -1, 17, -1, 15, -1]
r3  = [ 4,  8,  6,  3,  1,  6, 10,  6, 10,  2,  6, 10,  4,  1,  5,  5]

#r3s is kinda down for whatever
r3s = [10, -1, 10, -1, 10, -1,  6, -1, 13, -1,  3, -1,  3, -1,  6, -1]#

#rotations shows [r1s + r2, r2s + r3, r3s]
rotations = [0, 0, 0]

def cover(bottom, slatted_top):
    combined = [0]*len(bottom)
    for pos, num in enumerate(slatted_top):
        if num >= 0:
            combined[pos] = slatted_top[pos]
        else:
            combined[pos] = bottom[pos]
    return combined
    
def sum_cols(row0, row1, row2, row3):
    summed = [0]*len(row0)
    for pos, num in enumerate(row0):
        summed[pos] = row0[pos]+row1[pos]+row2[pos]+row3[pos]
    return summed
    
def rotate(first, linked, clockwise_amt):
    first = deque(first)
    first.rotate(clockwise_amt)  
    if linked:
        linked = deque(linked)
        linked.rotate(clockwise_amt)
    return list(first), list(linked)
    
def check_win(row0, row1, row2, row3):
    col_totals = sum_cols(row0, row1, row2, row3)
    if all(col == 40 for col in col_totals):  
        return True
    else:
        return False

def print_victory():
    success_string = "Found the answer after {} attempts".format(attempts)
    print("="*len(success_string))
    print(success_string)
    print()
    print("rotations: " + str(rotations))  
    print("="*len(success_string))


# here's where all the magic happens
while True:
    if check_win(r0, cover(r1, r1s), cover(r2, r2s), cover(r3, r3s)):
        print_victory()
        exit()
    else:
        pass










