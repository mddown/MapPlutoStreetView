# MapPlutoStreetView
View Google Street View pictures using MapPluto in Esri Desktop

This py script is meant to be used as a script tool in ArcMap/ArcCatalog. The input MapPluto file needs to be located in a geodatabase. Although this script is intended to be run on a MapPluto fc any fc that contains an ‘Address’ and ZipCode’ field will work. As long as the Google Street View API can interpret the input location a .jpg should be returned.

This script will add a new field ‘StreetView’ to your fc with the path to the output .jpg for that MapPluto feature. You can then view these photos directly from ArcMap.
