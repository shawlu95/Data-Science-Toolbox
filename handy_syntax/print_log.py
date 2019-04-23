import sys, os

sys.stdout = open("outputs/out.txt","a")
print("this is a log message")

# cannot do this:
# sys.stdout.close()
# print("done")