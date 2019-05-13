import os
import sys

rename = False
if len(sys.argv) > 1:
    # accepts one additional argument
    rename = sys.argv[1] == "True"
    if rename: print("Will rename files.")

for i, fname in enumerate(os.listdir(".")):
    if fname == ".DS_Store": 
        continue

    tmp = fname.strip().replace(" ", "_").replace("-", "_").replace(":", "").lower()
    if fname != sys.argv[0] and tmp != fname:
        print("%s \t -> %s"%(fname, tmp))
        
        # danger: rename files:
        if rename: os.rename(fname, tmp)
