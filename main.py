#задача 1 - дні тижня

try:
  print("1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday")
  user_select = int(input("Enter menu number: "))
  match user_select:
          case 1:
              print("Monday!")
          case 2:
              print("Tuesday!")
          case 3:
              print("Wednesday!")
          case 4:
              print("Thursday!")
          case 5:
              print("Friday!")
          case 6:
              print("Saturday!")
          case 7:
              print("Sunday!")
          case _:
              print("Incorrect menu item!")
except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(f"Error: {e}")
