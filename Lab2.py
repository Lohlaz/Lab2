import statistics

import statistics

print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")





def funcName(parameter1, parameter2):
    print("this is a dummy function")
    return 10

def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height* height)
    print("BMI = " + str(bmi))
    if (bmi < 18.5):
        print("Under Weight")
        return -1
    elif (bmi > 25.0):
        print("Over Weight")
        return 1

    else:
        print("Normal Weight")
        return 0


def display_main_menu():
    print("Hello, Please remember to seperate each readings/value with a space")
    return_value = get_user_input()
    calc_average_temperature(return_value)
    calc_min_max_temperature(return_value)
    sort_temperature(return_value)
    calc_median_temperature(return_value)



def get_user_input():
    print('Please Enter Your Temperatures:')
    inputa = input()
    print('Your Inputs: ' + inputa)
    split_input = inputa.split()
    res = list(map(float, split_input))
    listofvalues = res
    return listofvalues



def calc_average_temperature(listofvalues):
    no_of_inputs = len(listofvalues)
    total_value = 0;
    for x in listofvalues:
        total_value = total_value + x
    average = total_value/no_of_inputs
    print("Your Average Temperature Is: " + str(average))

def calc_min_max_temperature(listofvalues):
    small = min(listofvalues)
    big = max(listofvalues)
    print("Min = " + str(small))
    print("Max = " + str(big))

def sort_temperature(listofvalues):
    listofvalues.sort()
    for x in listofvalues:
        print(str(x) + ",")

def calc_median_temperature(listofvalues):
    print("Median = " + str(statistics.median(listofvalues)))



if __name__ == "__main__":
    display_main_menu()










