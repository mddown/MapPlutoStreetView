import arcpy
import urllib
import os

inFeat = arcpy.GetParameterAsText(0)
fields = ['Address', 'ZipCode']
addressList = []

#output Dir for photos
dir = arcpy.GetParameterAsText(1)

# pitch for camera angle
pitch = arcpy.GetParameterAsText(2)

#checks if the dir variable (output path) above exists and creates it if it does not
if not os.path.exists(dir):
    os.makedirs(dir)
    
#this is the first part of the streetview, url up to the address, this url will return a 600x600px image
pre="http://maps.googleapis.com/maps/api/streetview?size=600x600&location="
#this is my API key, please replace the one below with your own (google 'google streetview api key'), thanks!
suf="&pitch="+ pitch +"&amp;key=AIzaSyDHHRR7YNKTaNVICE3QmfDKTvzMenapO4w"

arcpy.AddField_management(inFeat, "StreetView", "TEXT", "#", "#", "500")

with arcpy.da.SearchCursor(inFeat, fields) as cursor:
    for row in cursor:
        address = ('{0},{1}'.format(row[0],row[1]))
        #print address
        #addressList.append(address)
        #print('{0},{1}'.format(row[0],row[1]))
        ln = address.replace(",","")
        URL = pre+ln+suf
        #creates the filename needed to save each address's streetview image locally
        filename = os.path.join(dir,ln+".jpg")
        urllib.urlretrieve(URL, filename)
        filename = filename.replace('\\', '/')
        addressList.append(filename)
        
print addressList
arcpy.AddMessage(addressList)
        
rows = arcpy.UpdateCursor(inFeat)
x = 0
for row in rows:
    row.setValue("StreetView", addressList[x])
    rows.updateRow(row)
    x = x+1

del row
del rows
del cursor

#arcpy.EnableAttachments_management(inFeat)    
#arcpy.AddAttachments_management(inFeat, "StreetView", inFeat, "StreetView", "StreetView")

print 'all done'
arcpy.AddMessage('ALL DONE')