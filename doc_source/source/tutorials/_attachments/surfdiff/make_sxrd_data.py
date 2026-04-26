'''Making sxrd data for simulations
P4mm symmetry k<h
'''
from numpy import c_, r_, array, arange, ones, savetxt

# Output filename at the same location as this script
outfile = 'rods.dat'

# h and k are integers, l is a float
h_min = 0
h_max = 3

k_min = 0
k_max = 3

l_min = 0.1
l_max = 3.5
l_step = 0.05

# Generate the l values
l = arange(l_min, l_max + l_step, l_step)


rods = array([[0,0,0,0,0]])[0:0]

# Generate the rods for h and k in the specified ranges
for h in range(h_min, h_max + 1):
    for k in range(k_min, h+1):
        rods = r_[rods, c_[h*ones(l.shape), k*ones(l.shape), l, l*0, l*0]]

savetxt(outfile, rods)
