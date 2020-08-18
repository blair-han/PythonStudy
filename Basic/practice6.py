## Dealing with Error

try:
    print("This is a calculator only for division.")
    nums = []
    nums.append(int(input("Type first number : ")))
    nums.append(int(input("Type second number : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error! wrong value!")
except ZeroDivisionError as err:
    print(err)
except:
    print("Unknown error!!!")



## User defined error 
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("This is a calculator noly for signle digit division")
    num1 = int(input("Type first number : "))
    num2 = int(input("Type second number : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input : {0}, {1}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("Wrong number! type single digit")
except BigNumberError as err:
    print("Wrong number! type single digit")
    print(err)
finally:
    print("Thank you for usint this calculator")
