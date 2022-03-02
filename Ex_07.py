def sum_of_numbers(limit):
  total = 0
  for i in range(limit+1):
      if i % 3 == 0 or i % 5 == 0:
        total = total + i
  return total
x = int(input("Enter limit: "))
print(sum_of_numbers(x))