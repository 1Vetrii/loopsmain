import sys
infile = "systm/dgjkhe82y/tmp/input8.txt"
sys.stdin = open (infile)
#----------------------------------
g = "~"
for i in str(input()):
  if i<g:
    g = i
print(g)