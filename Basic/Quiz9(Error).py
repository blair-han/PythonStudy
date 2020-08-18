## Chicken order system

class SoldOutError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Sold out! We are not taking an order anymore."

chicken = 10
waiting = 1 # waiting number starts from 1. 
while(True):
    print("Stock : {}".format(chicken))
    try:
        order = int(input("How many chicken do you want?"))
        if order<1:
            raise ValueError
        elif chicken == 0:
            raise SoldOutError

        if order > chicken:
            print("Out of stock!")
        else:
            print("[Waiting number {}] {} X Chicken has been ordered" \
                .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("You input is wrong!")
        continue
    except SoldOutError as err:
        print(err)
        break
    