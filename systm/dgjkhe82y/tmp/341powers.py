option = int(input())

if option == 1:
  num = int(input())
  power = int(input())
  answer = num**power
  if power == 0 or power == 1:
    print(f"{num}^{power}={answer}")
  else:
    print(f"{num}^{power}="+((str(num)+"*")*(power-1))+f"{num}={answer}")

if option==2:
  num = int(input())
  power = 0
  for i in range(11):
    answer = num**power
    if power == 0 or power == 1:
      print(f"{num}^{power}={answer}")
    else:
      print(f"{num}^{power}="+((str(num)+"*")*(power-1))+f"{num}={answer}")
    power=power+1