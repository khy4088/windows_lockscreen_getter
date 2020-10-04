import os
from os import rename, listdir
import shutil
from datetime import datetime
from PIL import Image

origin = os.getenv('LOCALAPPDATA') + '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
export_location = datetime.today().strftime("%Y%m%d%H%M%S")[2:]

shutil.copytree(origin,  export_location)

for filename in os.listdir(export_location):
    i = Image.open(export_location + '/' + filename)
    width, height = i.size
    print(width, height)
    i.close()
    if width < 700 or height < 700:
        os.remove(export_location + '/' + filename)
    else:
        os.rename(export_location + '/' + filename, filename + '.jpg')
        
os.rmdir(export_location)