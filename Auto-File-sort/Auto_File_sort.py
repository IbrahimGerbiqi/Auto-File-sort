from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
        i = 1
        def on_modified(self,event):
            for filename in os.listdir(folder_to_track):
                name, extension = os.path.splitext(filename)
                print(filename,name,extension)
                if extension == ".txt":
                    src = folder_to_track + "/" + filename
                    new_destination = folder_txt_destination + "/" + filename
                    os.rename(src, new_destination)
                if (extension == ".jpg" or extension == ".png"): 
                    src = folder_to_track + "/" + filename
                    new_destination = folder_images_destination + "/" + filename
                    os.rename(src, new_destination)



folder_to_track = "/Users/Lenovo/Desktop/"
folder_txt_destination = "/Users/Lenovo/Desktop/txtFolder"
folder_images_destination = "/Users/Lenovo/Desktop/imagesFolder"

evenet_handler = MyHandler()
observer = Observer()
observer.schedule(evenet_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print('its true')
except KeyboardInterrupt:
    observer.stop()
observer.join()
