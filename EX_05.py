def fizz_buzz(input):
    if input % 5 == 0:
        return 'Buzz'
    if input % 3 == 0:
        return 'Fizz'
    if (input % 3 == 0) and (input % 5 == 0):
        return 'Fizz_Buzz'
    return input
    

num = int(input("enter number : "))
result = fizz_buzz(num)
print(result)

#hello
