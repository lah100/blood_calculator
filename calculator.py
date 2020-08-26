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
    HDL_analysis = check_HDL(HDL_result)
    HDL_output = output_HDL(HDL_result, HDL_analysis)

def input_HDL():
    print("Check your HDL value:")
    HDL_value = input("Enter your HDL value: ")
    return int(HDL_value)

def check_HDL(HDL_testval):
    if HDL_testval >= 60 :
	    return "Normal"
    elif 40 <= HDL_testval <60 :
        return "Borderline Low"
    else :
	     return "Low"

def output_HDL(test_result, analysis) :
    print("The HDL result is {}".format(test_result))
    print("This HDL is {}".format(analysis))

interface()
