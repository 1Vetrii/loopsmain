num = int(input())
g = num
while num>=0:
  num = int(input())
  if num > g:
    g = num
print(g)