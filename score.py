'''
@author: bhoff
'''

import numpy as np
import os
import sys


if __name__ == '__main__':
    table = np.loadtxt('/metadata/images_crosswalk.tsv', dtype='str', skiprows=1)
    print("size of array: ", len(table))
    f = open('/output/out.txt', 'w')
    f.write("subjectId\tlaterality\tprediction\n")
    for i in range(0, len(table)):
        f.write('%s\t%s\t0\n' % (table[i][0], table[i][0]))
    f.close()
            