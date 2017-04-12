![Toolbox Icon](https://raw.githubusercontent.com/UN-OCHA/COD-ArcTools/master/Screenshots/ToolboxIcon/ArcToolBox.png)
# COD-ArcTools

A set of ArcGIS scripts created to automate certain points of the ITOS Administrative Boundaries Data Pre-processing evaluation.

The ITOS Administrative Boundaries Data Pre-processing Evaluation Checklist is used to evaluate essential characteristics of administrative boundary shapefiles before they are accepted into the collection of Common Operational Datasets (CODs).

To learn how use any of the scripts below, or to learn how to import a custom toolbox into ArcMap, refer to the **Tutorials** folder.

## UTF Encoding & Spatial Reference Check Toolbox
The *UTF_and_SpatialRefCheck.tbx* contains two scripts that check and report the UTF Encoding and Spatial Reference System for every shapefiles within a folder.

#### ITOS Data Pre-processing Coverage
ITOS checkpoints covered by *UTF_and_SpatialRefCheck.tbx*
* **1.4:** Encoding is in UTF-8 or higher
* **1.5:** Projection is defined, correct, and consistent

#### UTF Encoding Check Script Summary
The *UTF Encoding Check* script reports the UTF encoding of all shapefiles within a folder. The script works by first identifying each *.shp* file within the specified folder. The script then locates and reads each corresponding *.cpg* file to determine the UTF encoding. The UTF encoding for each shapefile is then reported to the user in the Details pane of the Results dialog box that appears when the script is used in ArcMap.

#### Spatial Reference System Check Script Summary
The *Spatial Reference System Check* script reports the UTF Spatial Reference System of each shapefiles within a folder. The script works by first identifying each *.shp* file within the specified folder, then identifies the Spatial Reference System used by each shapefile. The Spatial Reference System for each shapefile is then reported to the user in the Details pane of the Results dialog box that appears when the script is used in ArcMap.
