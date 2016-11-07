'''
@author: bhoff
'''

import csv
import os
import time

if __name__ == '__main__':
    crossWalkPath='/metadata/images_crosswalk.tsv'
    if not os.path.isfile(crossWalkPath):
        raise Exception(crossWalkPath+' does not exist')
    
    time.sleep(120) # sleep for two minutes

    with open(crossWalkPath,'r') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        f = open('/output/out.txt', 'w')
        f.write("subjectId\tlaterality\tprediction\n")
        first=True
        for row in tsvin:
            if first: # skip the header row
                first=False
                continue
            f.write('%s\t%s\t0\n' % (row[0], row[3]))
            imageFile='/scoringData/'+row[4]
            if not os.path.isfile(imageFile):
                raise Exception(imageFile+' does not exist')
    f.close()
        
