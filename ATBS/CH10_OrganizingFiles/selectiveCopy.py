#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with a
# certain file extension (such as .pdf or .jpg). Copies these files from
# whatever location they are in to a new folder.

import shutil, os
from pathlib import Path

def selectiveCopy(folder):

    # Copy PDF files in a foder tree to a new folder.

    folder = os.path.abspath(folder)   # make sure folder is absolute
    p = Path(folder)
    newFolder = os.path.basename(folder) + '_pdfs'
    os.mkdir(p.parent / newFolder)

    print('Searching for pdf files in %s' % (folder))
    for pdf in list(p.glob('**/*.pdf')):
        print('Copying %s to %s' % (pdf, p.parent / newFolder))
        shutil.copy(pdf, p.parent / newFolder)

    print('Done')

selectiveCopy(folder)
