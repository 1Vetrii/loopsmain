num = int(input())
c=1
for i in range(num):
  print(f"{c}:",end="")
  for a in range(c):
    print("A",end="")
  c=c+1
  print()