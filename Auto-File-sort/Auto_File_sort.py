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
                print(extension)
                print(name)
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)



folder_to_track = "/Users/Lenovo/Desktop/myFolder"
folder_destination = "/Users/Lenovo/Desktop/newFolder"
evenet_handler = MyHandler()
observer = Observer()
observer.schedule(evenet_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()
observer.join()
