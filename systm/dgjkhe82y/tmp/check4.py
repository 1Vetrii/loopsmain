import sys
infile = "systm/dgjkhe82y/tmp/input4.txt"
sys.stdin = open (infile)
#----------------------------------
w = 0
l = 0
t = 0
for i in str(input()):
  if i=="W":
    w = w+1
  if i=="L":
    l = l+1
  if i=="T":
    t = t+1

p=((w*3)+(l)+(t*2))
print(f"W-L-T\n{w}-{l}-{t}\nPoints: {p}")