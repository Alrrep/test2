#!/usr/bin/env python3
#by alumnos@ENES-FC206-15
# GNU/GPL License

import numpy as np
data_list=np.arange(1,11,1)
for x in data_list:
    print("value: " + str(x))
#z=np.cos(x)
x="Hola"

try:
    z=int(x)+1
except:
    print("Error in sum of z.")

print(data_list)
