# Author: Daniel Soden
# Purpose: Book Exam 

# Import statements

from myfunctions import *

# Main functions 

def get_teacher_and_class():
    teacher_name = get_non_empty_string("What is the teacher's name?  ")
    class_no = get_non_empty_string("What class are these students in?  ")
    in_class = get_positive_integer("How many students are in this class?  ")

    return teacher_name, class_no,in_class

def get_names_and_numbers(students:int):
    children_names = []
    no_books_read = []
    
    for child in range(students):
        child_name = get_non_empty_string("What is this child's name?  ")
        reading = get_positive_integer(f"How many books has {child_name} read?  ")
        children_names.append(child_name)
        no_books_read.append(reading)

    return children_names, no_books_read

def show_results_over_three(children_names:list, no_books_read:list):

    greater_three_list = []

    for i,count in enumerate(no_books_read):
        if count >= 3:
            greater_three_list.append(children_names[i])

    return greater_three_list

def get_average(no_books_read:list):
    total = 0
    for book_count in no_books_read:
        total += book_count

    average = total/len(no_books_read)

    return average


# Output: 

def main():
    teacher_name, class_no, in_class = get_teacher_and_class()
    names,books_read = get_names_and_numbers(in_class)
    best_students = show_results_over_three(names,books_read)
    print(best_students)
    average = get_average(books_read)
    print(f"The average number of books read is {average}")


if __name__ == "__main__":
    main()
