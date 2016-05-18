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
                firsttime=True
                for label in ['PatientID', 'StudyDate', 'PatientAge', 'SeriesDescription']:
                    if (firsttime):
                        firsttime=False
                    else:
                        sys.stdout.write(', ')
                    sys.stdout.write("{}: {}".format(label, RefDs.get(label)))
                print("")
                