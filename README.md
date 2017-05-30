# COD-ArcTools
A set of ArcMap scripts designed to automate certain steps of the ITOS Administrative Boundaries Data Pre-processing Checklist.

The ITOS Administrative Boundaries Data Pre-processing Checklist is used to evaluate essential characteristics of administrative boundary shapefiles before they are considered for acceptance into the collection of Common Operational Datasets (CODs).

To learn how use any of the scripts below, or to learn how to import a custom toolbox into ArcMap, refer to the [Tutorials Folder](/Tutorials).

 Only the *.tbx* files needs to be downloaded and imported into ArcMap. For convenience, the Python scripts that were embedded into the ArcMap tools are available in the [Python Folder](/Python). Editing the Python scripts found within the Python folder will not affect the functions of the tools within the *.tbx* files. Each *.tbx* file is independent and self-contained.

## UTF Encoding & Spatial Reference Check Toolbox
The *UTF_and_SpatialRefCheck.tbx* contains two scripts that each automate a step of the ITOS Administrative Boundaries Data Pre-processing Checklist check. Each script checks specific characteristics of every shapefile within a folder and then generates a report.

### ITOS Data Pre-processing Coverage
ITOS checkpoints covered by *UTF_and_SpatialRefCheck.tbx*
* **1.4:** Encoding is in UTF-8 or higher
* **1.5:** Projection is defined, correct, and consistent

### UTF Encoding Check Script Summary
The *UTF Encoding Check* script reports the UTF encoding of each shapefile within a folder.

The *UTF Encoding Check* script works by first identifying each *.shp* file within the specified folder. The script then locates and reads each corresponding *.cpg* file to determine the UTF encoding. The UTF encoding  is reported to the user in the Details pane of the Results dialog window that appears when the script is used in ArcMap v10.0 or later. [Tutorial](/Tutorials/UTF_EncodingCheck_Tutorial.md)

### Spatial Reference System Check Script Summary
The *Spatial Reference System Check* script reports the Spatial Reference System of each shapefile within a folder.

The *Spatial Reference System Check* script works by first identifying each *.shp* file within the specified folder. The script then identifies the Spatial Reference System used by each shapefile and reports the results to the user in the Details pane of the Results dialog window that appears when the script is used in ArcMap v10.0 or later. [Tutorial](/Tutorials/SpatialRefCheck_Tutorial.md)
