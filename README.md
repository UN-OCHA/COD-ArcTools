# COD-ArcTools

A set of ArcGIS scripts that automate certain points of the ITOS COD evaluation checklist.

## ITOS Administrative Boundaries Data Pre-processing
A list of checkpoints that evaluate basic and essential characteristics of administrative boundary shapefiles.
### UTF Encoding & Spatial Reference Check Toolbox
The *UTF_and_SpatialRefCheck.tbx* contains two scripts that check and report the UTF Encoding and Spatial Reference System for all shapefiles within a folder.
#### ITOS Data Pre-processing Coverage
Checkpoints covered by *UTF_and_SpatialRefCheck.tbx*
* **1.4:** Encoding is in UTF-8 or higher
* **1.5:** Projection is defined, correct, and consistent

#### UTF Encoding Check Script
The *UTF Encoding Check* Script reports the UTF encoding of all shapefiles within a folder. The script works by first identifying each *.shp* file within the specified folder. The script then locates and reads each corresponding *.cpg* file to determine the UTF encoding. The UTF encoding for each shapefile is then reported to the user in the details pane of the Results dialog box in the following format:
> \*\*\*\*\*RESULTS\*\*\*\*\*

> There are 00 .shp files and 00 .cpg files in:
> D:\\UN\\OSM_Data\\Humanitarian_OSM_Export\\Haiti\\haiti_shp

> planet_osm_line.shp is encoded with UTF-8
> planet_osm_point.shp is encoded with UTF-8
> planet_osm_polygon.shp is encoded with UTF-8


>\*\*\*\*\*RESULTS\*\*\*\*\*
