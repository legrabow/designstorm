#
# Provide :
#    1) "tot_duration" for the total time of the storm
#    2) "disc" for the discretization in time
#    3) "P24" to parameterize the IDF curve
#
# Get:
#    1) "ts" for precipitation time series

import numpy as np

def intensity(drt):
    its = P24 / 24 * 11**((28**0.1-drt**0.1)/(28**0.1-1))
    return its

P24 = 165 # in mm
tot_duration = 24 # in h
disc = 15 / 60 # in h

cum_sum = 0
precs = np.array([])
for drt in np.arange(disc, tot_duration + disc, disc):
    its = intensity(drt)
    prec = its * drt - cum_sum
    cum_sum = its * drt
    precs = np.append(precs, prec)

precs_sorted = np.flip(np.sort(precs))
ts = np.zeros_like(precs)
middle_idx = int(np.floor(len(ts) / 2))

sign = -1
pos = 0
for prec in precs_sorted:
    sign = sign * (-1)
    ts[middle_idx + sign * pos] = prec
    if sign == 1:
        pos += 1
