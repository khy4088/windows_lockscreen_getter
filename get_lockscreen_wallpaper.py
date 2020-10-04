import os
from os import rename, listdir
import shutil
import sys
from datetime import datetime

origin = os.getenv('LOCALAPPDATA') + '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
export_location = datetime.today().strftime("%Y%m%d%H%M%S")[2:]

shutil.copytree(origin,  export_location)

for filename in os.listdir(export_location):
    print(filename)
    if os.path.getsize(export_location + '/' + filename) / 1024 < 200:
        os.remove(export_location + '/' + filename)

for remain in os.listdir(export_location):
    os.rename(export_location + '/' + remain, export_location + '/' + remain + '.jpg')
