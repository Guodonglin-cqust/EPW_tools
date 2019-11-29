#!/usr/bin/env python2

import numpy as np
N = 6
for ii in np.arange(0,1.0,1.0/N):
    for jj in np.arange(0,1.0,1.0/N):
        print ii,' ',jj, ' 0.0 ',1.0/(N**2)
        