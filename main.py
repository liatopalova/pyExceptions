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

# задача 2 - рівність чисел

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if (num1 == num2):
        print("Numbers are equal!")
    else:
        if (num1 > num2):
            print(num2, num1, sep=", ")
        else:
            print(num1, num2, sep=", ")
except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(f"Error: {e}")

# задача 3 - математична дія

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number:"))
    print("1. +\n2. -\n3. *\n4. /\n")
    user_choice = int(input("Enter menu operation:  "))
    result = 0
    match user_choice:
        case 1:
            result = number1 + number2
            print(f"Sum: {result}")
        case 2:
            if (number1 > number2):
                result = number1 - number2
            elif (number1 < number2):
                result = number2 - number1
            else:
                result = number2 - number1
            print(f"Difference: {result}")
        case 3:
            result = number1 * number2
            print(f"Mult: {result}")
        case 4:
            try:
                if (number1 > number2):
                    result = number1 / number2
                elif (number2 > number1):
                    result = number2 / number1
                else:
                    result = number1 / number2
                print(f"Division: {result}")
            except ZeroDivisionError:
                print("Enter non-zero number!")
        case _:
            print("Incorrect menu item!")


except ValueError:
    print("Enter only numbers please!")
except Exception as e:
    print(f"Error: {e}")
