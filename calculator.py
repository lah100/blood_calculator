def interface():
    print("My Program")
    while True:
        print("Option:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()

def HDL_driver():
    # get input
    # check if HDL is normal
    # output
    HDL_result = input_HDL()
def input_HDL():
    print("Check your HDL value:")
    HDL_value = input("Enter your HDL value: ")
    return int(HDL_value)
    check_HD

interface()
