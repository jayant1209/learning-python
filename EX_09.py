def prime_number(limit):
  for i in range(limit):
    if i % 2 != 0:
      print(i)
x=int(input("Enter Limit: "))
prime_number(x)