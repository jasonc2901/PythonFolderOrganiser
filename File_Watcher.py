import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import shutil


class File_Watcher:

    #replace with a valid folder on your machine
    DIRECTORY_TO_WATCH = "/path/to/your/directory"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print "Error"

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            # Take any action here when a file is first created.
            print "Received created event - %s." % event.src_path
            
            file = event.src_path

            #replace with valid paths for each sub folder within your DIRECTORY_TO_WATCH 
            if ".jpg" in file:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/images")
            elif ".py" in file:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/python")
            elif ".docx" in file:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/Word")
            elif ".java" in file:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/Java")
            elif ".pdf" in file:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/pdf")
            else:
                shutil.move(file,"/path/to/DIRECTORY_TO_WATCH/other")

    
if __name__ == '__main__':
    w = File_Watcher()
    w.run()