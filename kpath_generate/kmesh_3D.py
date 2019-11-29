#!/usr/bin/env python2

import numpy as np
N = 6
for ii in np.arange(0,1.0,1.0/N):
    for jj in np.arange(0,1.0,1.0/N):
        for kk in np.arange(0,1.0,1.0/N):
            print ii,' ',jj, ' ',kk, ' ',1.0/(N**3)
