a=0
e=0
i=0
o=0
u=0
oth=0
for letter in str(input()):
  if letter=="a":
    a = a+1
  elif letter=="e":
    e = e+1
  elif letter=="i":
    i = i+1
  elif letter=="o":
    o = o+1
  elif letter=="u":
    u = u+1
  else:
    oth = oth+1

print(f"a: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}\nothers: {oth}")