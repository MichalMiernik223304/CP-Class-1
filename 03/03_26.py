pin = "0805"
posibilities = 3
pin_try = 0

for i in range(1, posibilities + 2):

    pin_try = input("Enter the PIN code: ")

    if i < posibilities and pin_try == pin:
        print("PIN Correct")
        break
    elif i < posibilities and pin_try != pin:
        print("Incorrect!")
    else:
        print("Incorrect...\nSorry, your payment card has been blocked!")
        break
