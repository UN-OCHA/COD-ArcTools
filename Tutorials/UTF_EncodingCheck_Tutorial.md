# ArcMap Tool Tutorial:  UTF Encoding Check

## UTF Encoding Check Script Summary
The *UTF Encoding Check* script reports the UTF encoding of all shapefiles within a folder. The script works by first identifying each *.shp* file within the specified folder. The script then locates and reads each corresponding *.cpg* file to determine the UTF encoding. The UTF encoding for each shapefile is then reported to the user in the Details pane of the Results dialog box that appears when the script is used in ArcMap v10.0 or newer.

### 1. Files to be Processed
![Files Image](K:\UN\UN_COD_Tools\COD-ArcTools\Screenshots\SpatialRef_Check\files.PNG "Files to be Processed")

For this example, there are three different types of shapefiles (line, point, polygon) within a folder titled *Haiti_shp*. The *UTF Encoding Check* script will report each shapefile's UTF encoding when used in ArcMap.

### 2. Opening the UTF Encoding Check Script
To open the script, double-click the *UTF Encoding Check* script within the *UTF and Spatial Ref Check* toolbox.

![Toolboxes Image](K:\UN\UN_COD_Tools\COD-ArcTools\Screenshots\UTF_Check\toolAdded.PNG "Toolboxes")

When the *UTF Encoding Check* script interface is displayed, it should look like the image below.

![UTF Check UI Image](K:\UN\UN_COD_Tools\COD-ArcTools\Screenshots\UTF_Check\UTFCheckUI.PNG "UTF Check UI")

### 3. Specifying the Folder to Evaluate & Executing the Script
Navigate to the folder that contains the shapefiles that you wish to check the UTF encoding of. In this tutorial, the folder to specify is the *Haiti_shp* folder. Click 'Add' then 'OK' to run the *UTF Encoding Check* script on each shapefile within the specified folder.

Note 1: The *UTF Encoding Check* script does not evaluate any shapefiles that may be within sub-folders.

![Selecting a folder Image](K:\UN\UN_COD_Tools\COD-ArcTools\Screenshots\UTF_Check\UTFChooseFolder.PNG "Selecting a folder")


Note 2: The if each shapefile does not have a corresponding *.cpg* file, you will be notified with one of the following messages:.

If there are a different number of *.shp* and *.cpg* files within the specified folder:

	There are uneven totals for .shp files and .cpg files.
	Please make sure there is a .cpg file for each .shp in
	the folder before running the UTF Check tool again.

If there are an equal number of *.shp* and *.cpg* files within the specified folder, but not every *.shp* file has a matching *.cpg* file:

	The UTF encoding information for XXXXX.shp could not be found.
	Since the number of .shp files matches the number of .cpg files, perhaps
	the names of the .shp file and .cpg file do not match.

### 4. Viewing the Results
Once the *UTF Encoding Check* script has finishing running, it will display the name and UTF encoding of each shapefile. Check the displayed results to ensure that each shapefile is using the correct UTF encoding. In this tutorial, all three shapefiles are encoded with *UTF-8*.

Note: If the results window closes automatically, the results can also be found in the *Geoprocessing Results Window* which can be activated by clicking *Geoprocessing -> Results* from the menu bar found at the top of the screen.

	Executing: UTFcheck "D:\UN\OSM Data\Humanitarian OSM Export\Haiti\haiti_shp"

	Running script UTFcheck...


	*****RESULTS*****

	There are 3 .shp files and 3 .cpg files in:
	D:\UN\OSM_Data\Humanitarian_OSM_Export\Haiti\haiti_shp

	planet_osm_line.shp is encoded with UTF-8
	planet_osm_point.shp is encoded with UTF-8
	planet_osm_polygon.shp is encoded with UTF-8


	*****RESULTS*****

	Completed script UTFcheck...

![Selecting a folder Image](K:\UN\UN_COD_Tools\COD-ArcTools\Screenshots\UTF_Check\UTFOutput.PNG "Selecting a folder")

### Tutorial Complete
