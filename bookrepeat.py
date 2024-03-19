# Author: Daniel Soden
# Purpose: Python Exam week 8

# Import statements

from myfunctions import *

# Main functions

def get_teacher_and_class():
    """This function asks the user for the name of the teachcer 
       and what class their in (1st to 6th class)
    """
    teacher_name = get_non_empty_string("What is the teacher's name?  ")
    class_num = get_positive_integer(f"What class are they in (1-6)")

    print(f"Mr/Mrs {teacher_name} is the one teaching class {class_num}!")

def get_names_numbers():
    student_names = []
    books_read = []
    
    num_of_students = get_positive_integer("How many students are in the school?  ")

    for i in range(num_of_students):
        name = get_non_empty_string("What is their name?  ")
        book_no = get_positive_integer(f"How many books has {name} read?  ")
        student_names.append(name)
        books_read.append(book_no)
    return student_names,books_read

def show_results_over_three(student_names:list,books_read:list):
    best_students = []

    for i,num_read in enumerate(books_read):

        if num_read >= 3:
            best_students.append(student_names[i])
        else:
    pass

    return best_students

def get_average(books_read:list,student_names:list):

    total = 0

    for value in books_read:
        total += books_read

    average = total/len(student_names)

    return average

# Output

def main():
    pass

if __name__ = "__main__":
    main()
