from forex_python.bitcoin import BtcConverter
b = BtcConverter()

while True:
    user_name = input("Enter Your Name: ")
    if (user_name == ""):
        print("Enter Your Name Please !!!")
        continue
    else:
        user_amount = int(input("Enter Amount:"))
        if (user_amount<=0):
            print("Enter Valid Amount {user_name}".format(user_name=user_name))
            break
        else:
            print("Today BTC Price : USD",b.get_latest_price('EUR'))
            print("Your Purchased BTC : ",b.convert_to_btc(user_amount, 'USD'))

            #get user input to run or quit program
            print("Press q or a , q = quit | a = run again")
            promt = input("Enter q or a: ")
            if promt=="q":
                break
            elif promt=="a":
                continue
            else:
                print("Wrong Input !")


    
