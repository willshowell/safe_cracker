# crack.py 
#
# each 'row' is listed as an array. some are physically linked. a -1 
# means that nothing exists in that space.
#
# r0:  outer row
# r1:  next most outer row - physically connected to r0
# r1s: can overlap r1 and is slotted
# r2:  inside the r1 row but is connected to r1s
# ....and so on
#

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


def cover(bottom, slatted_top):
    combined = [0]*len(bottom)
    for pos, num in enumerate(slatted_top):
        if num >= 0:
            combined[pos] = slatted_top[pos]
        else:
            combined[pos] = bottom[pos]
    return combined

print(cover(r1, r1s))
