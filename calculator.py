def interface():
    print("My Program")
    while True:
        print("Option:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()

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

def LDL_driver():
# get input
    LDL_input = input_LDL()
# analyze
    LDL_analysis = check_LDL(LDL_input)
# display output
    LDL_output = output_LDL(LDL_input, LDL_analysis)

def input_LDL():
	print("Check your LDL value")
	LDL_value = input("Enter your LDL value: ")
	return int(LDL_value)

def check_LDL(LDL_value):
	if LDL_value < 130 :
		return "Normal"
	elif 130 <= LDL_value < 160 :
		return "Borderline High"
	elif 160 <= LDL_value < 190 :
		return "High"
	else :
		return "Very High"

def output_LDL(result, clin_analysis) : 
	print("The LDL result is {}".format(result))
	print("This LDL is {}".format(clin_analysis))

interface()
