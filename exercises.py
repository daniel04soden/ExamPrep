# Author: Daniel Soden
# Purpose: Exam Prep

# Import statments

from myfunctions import *
from random import randint

# Global Constants

HOURLY_RATE = 10.0

# Main functions

def lucky_draw(names_list:list):
    random_num = randint(0,len(names_list))

    choice = names_list[random_num]

    return choice

def phone_book(no_of_contacts:int):
    names_phone = []
    numbers_phone = []


    for i in range(no_of_contacts):
        name = get_non_empty_string(f"What is the name of this contact?  ")
        number = get_positive_integer(f"What is {name}\'s number?  ")

        names_phone.append(name)
        numbers_phone.append(number)
    
    print(f"{'Name':<15}{'Number':<15}")
    print('='*40)
    for i,number in enumerate(numbers_phone):
        print(f"{names_phone[i]:<15}{number:<15}")

def pay_slip():
    hours_worked = []
    list_of_earnings = []

    for i in range(0,7):
        hours_day = get_positive_float(f"How many hours did you work on day {i+1}  ")
        hours_worked.append(hours_day)

    for hours in hours_worked:
        pay = (hours*HOURLY_RATE) + 20
        
        if hours > 20:
            pay += 20
        else:
            pass

        list_of_earnings.append(pay)

    return list_of_earnings,hours_worked

def print_pay_slip(list_of_earnings:list):

    print(f"{'Day of Week':<10} {'Daily pay':<10}")
    print("="*30)
    for i,daily_earn in enumerate(list_of_earnings):
        print(f"{i+1:<10}{daily_earn:<10}")
    print(f"Total Pay: {sum(list_of_earnings):,.2f}")

# Main Output

def main():
    names = [
        "Daniel",
        "Sean",
        "Aoife",
        "Becca"
    ]
    no_of_contacts = get_positive_integer("How many contacts do you want to input?  ")
    phone_book(no_of_contacts)
    list_of_earnings,hours_worked = pay_slip()
    print_pay_slip(list_of_earnings)
    


if __name__ == "__main__":
    main()
