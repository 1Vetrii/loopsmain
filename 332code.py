v = input()
t = ""
for i in v:
  if i == "a":
    t = t+"b"
  if i == "b":
    t = t+"c"
  if i == "c":
    t = t+"d"
  if i == "d":
    t = t+"e"
  if i == "e":
    t = t+"f"
  if i == "f":
    t = t+"g"
  if i == "g":
    t = t+"h"
  if i == "h":
    t = t+"i"
  if i == "i":
    t = t+"l"
  if i == "l":
    t = t+"m"
  if i == "m":
    t = t+"n"
  if i == "n":
    t = t+"o"
  if i == "o":
    t = t+"p"
  if i == "p":
    t = t+"q"
  if i == "q":
    t = t+"r"
  if i == "r":
    t = t+"s"
  if i == "s":
    t = t+"t"
  if i == "t":
    t = t+"u"
  if i == "u":
    t = t+"v"
  if i == "v":
    t = t+"w"
  if i == "w":
    t = t+"x"
  if i == "x":
    t = t+"y"
  if i == "y":
    t = t+"z"
  if i == "z":
    t = t+"a"
  if i==" ":
    t = t+"*"
  if i<"a" or i>"z":
    if i!=" ":
      t = t+i
print(t)