"""
Spatial Reference Check
v1.0
Henry Mros
"""

import arcpy

arcpy.env.workspace = arcpy.GetParameterAsText(0)

shpFileList = arcpy.ListFiles("*.shp")

arcpy.AddMessage("\n\n*****RESULTS*****\n")

shpCount = 0

for shpFile in shpFileList:
    shpCount = shpCount + 1
    spatial_ref = arcpy.Describe(shpFile).spatialReference.name
    arcpy.AddMessage("{0} is {1}".format(shpFile, spatial_ref))

arcpy.AddMessage("\n{0} shapefiles found and checked within:\n{1}\n".format(shpCount,arcpy.env.workspace))
arcpy.AddMessage("\n*****RESULTS*****\n")