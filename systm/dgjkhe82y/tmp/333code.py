v = input()
t = ""
c = 0
for i in v:
  if i>="a" and i<"z":
    c=ord(i)+1
    t=t+chr(c)
  if i==" ":
    t = t+"*"
  if (i<"a" or i>"z") and i!=" ":
    t = t+i
print(t)