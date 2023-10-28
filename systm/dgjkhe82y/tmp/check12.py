import sys
infile = "systm/dgjkhe82y/tmp/input12.txt"
sys.stdin = open (infile)
#----------------------------------

num = int(input())
g = num
while num>=0:
  num = int(input())
  if num > g:
    g = num
print(g)