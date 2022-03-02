def drivers_speed(speed):
  if speed<75:
    print("ok")
  else:
    extra = speed - 70
    points = int(extra/5)
    if points > 12:
      print("L  canceled")
    else:
      print(points)
speed_input =int(input("enter speed :"))
drivers_speed(speed_input)