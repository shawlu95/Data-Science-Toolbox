import sys

sys.stdout = open("outputs/out.txt","a")
print("this is a log message")

sys.stdout.close()

# cannot do this:
# print("done")