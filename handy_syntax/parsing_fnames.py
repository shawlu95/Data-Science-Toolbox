import sys

p = lambda s: s.replace(" ", "_").replace("-", "_").replace("-", "").replace(":", "").lower()

for s in sys.argv[1:]:
	p(s)