# Author: Daniel Soden
# Purpose: Exam Practice

# Import Statements

from myfunctions import *

# All functions

def workers(num_workers:int):
    worker_names = []
    workers_hours = []
    hourly_rate = []

    for i in range(num_workers):
        name = get_non_empty_string(f"What is this worker number {i+1}\'s name?  ")
        hours = get_positive_float(f"How many hours did {name} work this week?  ")
        pay = get_positive_float(f"How much does {name} make an hour?  ")
        worker_names.append(name)
        workers_hours.append(hours)
        hourly_rate.append(pay)

    return worker_names,workers_hours,hourly_rate

def calculate_pay(workers_hours:list,hourly_rate:list):
    money_owed = []

    for i,money in enumerate(hourly_rate):
        payment_week = money*(workers_hours[i])

        if workers_hours[i] >= 30:
            payment_week += 20
        else:
            pass

        money_owed.append(payment_week)

    return money_owed

def allocate_pay(worker_names:list,money_owed:float):

    for i,pay in enumerate(money_owed):
        print(f"{worker_names[i]} is owed €{pay:,.2f}")

def calc_total_pay(money_owed:list):
    total = 0
    for money in money_owed:
        total += money 

    return total 

def calc_average_hours(workers_hours:list,worker_names:list):
    total_hours = 0 
    for hours in workers_hours:
        total_hours += hours
    average = total_hours/len(worker_names)

    return average

def worst_hours(workers_hours:list):
    worst_hours_worked = 0

    for hours in workers_hours:
        if hours < worst_hours_worked:
            worst_hours_worked = hours
        else:
            pass

    return worst_hours_worked




# Main Output

def main():
    num_workers = get_positive_integer("How many workers does Megan have?  ")
    worker_names,workers_hours,hourly_rate = workers(num_workers)
    money_owed = calculate_pay(workers_hours,hourly_rate)
    allocate_pay(worker_names,money_owed)
    print(f"{calc_total_pay(money_owed):,.2f}")
    print(f"{calc_average_hours(workers_hours,worker_names):,.2f} Hours have been worked on average")
    print(worst_hours(workers_hours))


if __name__ == "__main__":
    main()
