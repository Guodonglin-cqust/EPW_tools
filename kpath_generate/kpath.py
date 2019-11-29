#!/usr/bin/env python2

import numpy as np

nk=0.1/0.005
print int(nk)

for k in np.arange(0.0,0.1,0.005):
  print ' 0.0 '+str(k)+' '+str(k)+' 1.0'
