import time
import sys

for i in range(5):
    print(i),
    # needed in python2, not needed in python3
    #sys.stdout.flush()
    time.sleep(1)