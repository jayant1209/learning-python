b = int(input("num2 : "))
initialNum = b
sum = 0
while(b>0):
  digit = b % 10
  b = int(b / 10)
  sum = sum + (digit**3)


if sum==initialNum:
  print("ok")
else:
  print("no")