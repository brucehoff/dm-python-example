'''
Created on May 17, 2016

This takes from 
https://pyscience.wordpress.com/2014/09/08/dicom-in-python-importing-medical-image-data-into-numpy-with-pydicom-and-vtk/

@author: bhoff
'''

import dicom
import os
import sys

if __name__ == '__main__':
    #PathDicom = "/trainingData"
    PathDicom = sys.argv[1]
    for dirName, subdirList, fileList in os.walk(PathDicom):
        for filename in fileList:
            if ".dcm" in filename.lower():
                sys.stdout.write("{}: ".format(filename))
                RefDs = dicom.read_file(os.path.join(dirName,filename))
                # RefDs.dir has lots of info
                #print(RefDs.dir)
                firsttime=True
                sys.stdout.write('file size (MB): {}, '.format(os.path.getsize(dirName+"/"+filename)/1024000))
                for label in ['PatientID', 'StudyDate', 'PatientAge', 'SeriesDescription', 'Rows', 'Columns']:
                    if (firsttime):
                        firsttime=False
                    else:
                        sys.stdout.write(', ')
                    sys.stdout.write("{}: {}".format(label, RefDs.data_element(label).value))
                print("")
                