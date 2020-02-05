#! python3
# largeFileFinder.py - Walks through a folder tree and searches for
# exceptionally large files or folders (over 100 MB). Print these files with
# their absolute path to the screen.

import shutil, os
from pathlib import Path

def largeFileFinder(folder):

    # Find large files in folder tree.

    folder = os.path.abspath(folder)   # make sure folder is absolute

    for foldername, subfolders, filenames in os.walk(folder):

        for filename in filenames:
            # print('%s' % (os.path.join(foldername, filename)))
            if os.path.getsize(os.path.join(foldername, filename)) > 100000000:
                print('%s' % (os.path.join(foldername, filename)))






    print('Done')

largeFileFinder(folder)
