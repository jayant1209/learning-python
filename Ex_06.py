def Even_Odd(limit):
  for i in range(limit+1):
    if i==0:
      print(i,end=" ")
      print("EVEN")

    elif i%2==0:
        print(i,end=" ")
        print("EVEN")
    else:
        print(i,end=" ")
        print("ODD")
x=int(input("Enter limit: "))
Even_Odd(x)