num = int(input())
c=0
total=0
g=num
s=num
avg=0
lt=0
numl = num
while num!=-99999:
  c = c+1
  total = total+num
  avg = round(float(total/c),1)
  if num>g:
    g = num
  if num<s:
    s = num
  if num<numl:
    lt=lt+1
  num = int(input())

#print(f"Integers: {c}\nLargest: {g}\nSmallest: {s}\nTotal: {total}\nAverage: {avg}\nLess than {numl}: {lt}")

print("Integers:",c)
print("Largest:",g)
print("Smallest:",s)
print("Total:",total)
print("Average:",avg)
print("Less than "+str(numl)+": "+str(lt))
