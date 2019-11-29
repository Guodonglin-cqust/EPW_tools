<center> <font color=red, size=6>介绍各个脚本的用途 </font> </center>

## kgen.py
``` python
#!/usr/bin/env python2
#
# 14/07/2015  Samuel Ponce
#
import numpy as np

i=0
for ii in np.arange(0.5,0.0,-1.0/200):
  print str(ii)+' 0.0 0.0 '+str(1.0/201)
  i +=1

for ii in np.arange(0.0,0.5+1.0/200,1.0/200):
  print str(ii)+' '+str(ii)+' 0.0 '+str(1.0/201)
  i +=1

print i
```
<font color=blue> Note: 用于epw计算时产生指定高对称点路径上的点 </font>

## kpath.py
``` python
#!/usr/bin/env python2

import numpy as np

nk=0.1/0.005
print int(nk)

for k in np.arange(0.0,0.1,0.005):
  print ' 0.0 '+str(k)+' '+str(k)+' 1.0'
```
<font color=blue> Note: 用于epw计算时产生指定高对称点路径上的点 </font>

## kmesh_2D.py
``` python
#!/usr/bin/env python2

import numpy as np
N = 6
for ii in np.arange(0,1.0,1.0/N):
    for jj in np.arange(0,1.0,1.0/N):
        print ii,' ',jj, ' 0.0 ',1.0/(N**2)
```
<font color=blue> Note: 用于pwscf模块在做非自洽计算时产生k点，该脚本适用于二维材料计算，且保证产生的k点严格为正 </font>

## kmesh_3D.py
``` python
#!/usr/bin/env python2

import numpy as np
N = 6
for ii in np.arange(0,1.0,1.0/N):
    for jj in np.arange(0,1.0,1.0/N):
        for kk in np.arange(0,1.0,1.0/N):
            print ii,' ',jj, ' ',kk, ' ',1.0/(N**3)
```
<font color=blue> Note: 用于pwscf模块在做非自洽计算时产生k点，该脚本适用于体材料计算，且保证产生的k点严格为正 </font>

## kmesh.pl
``` perl
#!/usr/bin/perl -w


$numargs = $#ARGV+1; 

if (($numargs<3)||($numargs>4)) {
    print  "usage: n1 n2 n3 [wan]\n";
    print  "       n1  - divisions along 1st recip vector\n";
    print  "       n2  - divisions along 2nd recip vector\n";
    print  "       n3  - divisions along 3rd recip vector\n";
    print  "       wan - omit the kpoint weight (optional)\n";
    exit;
} 

if ($ARGV[0]<=0) {
    print "n1 must be >0\n";
    exit;
}
if ($ARGV[1]<=0) {
    print "n2 must be >0\n";
    exit;
}
if ($ARGV[2]<=0) {
    print "n3 must be >0\n";
    exit;
}

$totpts=$ARGV[0]*$ARGV[1]*$ARGV[2];

if ($numargs==3) {
    print "K_POINTS crystal\n";
    print $totpts,"\n";
    for ($x=0; $x<$ARGV[0]; $x++) {
	for ($y=0; $y<$ARGV[1]; $y++) {
	    for ($z=0; $z<$ARGV[2]; $z++) {
		printf ("%12.8f%12.8f%12.8f%14.6e \n", $x/$ARGV[0],$y/$ARGV[1],$z/$ARGV[2],1/$totpts);
	    }
	}
    }
}


if ($numargs==4) {
    for ($x=0; $x<$ARGV[0]; $x++) {
	for ($y=0; $y<$ARGV[1]; $y++) {
	    for ($z=0; $z<$ARGV[2]; $z++) {
		printf ("%12.8f%12.8f%12.8f \n", $x/$ARGV[0],$y/$ARGV[1],$z/$ARGV[2]);
	    }
	}
    }
}


exit;
```
<font color=blue> Note: 该脚本来源于wannier90软件包，用于pwscf模块在做非自洽计算时产生k点，适用于体材料和低维材料计算，且保证产生的k点严格为正 </font>
