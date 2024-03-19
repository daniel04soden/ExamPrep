# Author: Daniel Soden
# Purpose: Python Exam

# Import Statements

from myfunctions import *

# Main functions

def print_languages_and_popularity(list_languages:list,list_popularity):
    """This function prints the languages and their correspoding popularity 
       in a tabular format

       :param: list_languages: list of strings of various programminng languages
               list_popularity: list of the corresponding languages popularity 

        returns: None (Just prints)
    """

    print(f"{'Language':<15}{'Popularity':<15}")
    print("*"*40)

    for i,language in enumerate(list_languages):
        print(f"{language:<15}{list_popularity[i]:<15}")

def update_popularity(list_languages:list,list_popularity):
    language = True
    while language:
        language_input = get_non_empty_string("Enter the langauge you would like to change:  ")
        
        if language_input not in list_languages:
            print("Hey silly that isn't one of our languages!")
        else:
            new_popularity = get_non_empty_string(f"How popular is {language_input} now?  ")

            index_of_language = list_languages.index(language_input)

            list_popularity[index_of_language] = new_popularity
            language = False

    return list_popularity

def print_popular_languages(list_languages:list,list_popularity:list):
    popular_languages = []

    for i,popularity in enumerate(list_popularity):

        if popularity == "High":
            popular_languages.append(list_languages[i])
        else:
            pass
    return popular_languages
# Main Output

def main():
    list_languages = [
        "Java",
        "C++",
        "Python",
        "Ruby",
        "JavaScript"
    ]
    list_popularity = [
        "Medium",
        "Medium",
        "High",
        "Low",
        "High"
    ]
    print_languages_and_popularity(list_languages,list_popularity)
    print(update_popularity(list_languages,list_popularity))
    print(print_popular_languages(list_languages,list_popularity))

if __name__ == "__main__":
    main()
