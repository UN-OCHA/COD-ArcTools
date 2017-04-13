"""
UTF Encoding Check
v2.0
Henry Mros
"""

import sys, os, arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

path = arcpy.env.workspace

shpFileList = arcpy.ListFiles("*.shp")
cpgFileList = arcpy.ListFiles("*.cpg")

shpCount1 = 0
cpgCount1 = 0

arcpy.AddMessage("\n\n*****RESULTS*****\n")

for shpFile in shpFileList:
    shpCount1 = shpCount1 + 1 

for cpgFile in cpgFileList:
    cpgCount1 = cpgCount1 + 1

arcpy.AddMessage("There are {0} .shp files and {1} .cpg files in:\n{2}\n".format(shpCount1, cpgCount1, path))

if shpCount1 == cpgCount1:
    for shpFile in shpFileList:
        cpgFileName = shpFile.split(".")
        cpgFileName = str(cpgFileName[0]) + ".cpg"
        cpgFilePath = path +  "\\" + cpgFileName
        try:
            cpgFile = open(cpgFilePath, 'r')
            cpgContents = cpgFile.read()
            arcpy.AddMessage("{0} is encoded with {1}".format(shpFile, cpgContents))
        except:
            arcpy.AddMessage("\nThe UTF encoding information for {0} could not be found.\nSince the number of .shp files matches the number of .cpg files, perhaps the names of the .shp file and .cpg file do not match.\n".format(shpFile))
        
else:
    arcpy.AddMessage("There are uneven totals for .shp files and .cpg files.\nPlease make sure there is a .cpg file for each .shp in the folder before running the UTF Check tool again.")

arcpy.AddMessage("\n\n*****RESULTS*****\n")