# Author: Daniel Soden
# Purpose: BX Lab exam 

# Import statements

from myfunctions import *

# Actual functions

def print_languages_and_popularity(list_programming_languages:list,list_popularity:list):
    """This function prints the languages and popularity of
        a list of programming languages 

        param: list_programming_languages (list): list of programming languages
                list_popularity (list): list of populaity

        returns: None
    """

    print(f"{'Languages':^15}{'Popularity':^15}\n"
        f"{'='*30}\n")
    count = 0

    for i in list_programming_languages:
        print(f"{i:<15}{list_popularity[count]:<15}")
        count += 1

def update_popularity(language:str,list_programming_languages:list,list_popularity:list):
    """ this function takes the name of a language 
        and access the list of both programming languages and popularity of these languages
        and from here edits the popularity from user input 

        param: language (str): name of the language
        list_programming_languages (list): list of programming languages
        list_popularity (list): list of poplar programming languages 

    returns: updated popularity list 
    """
    if language in list_programming_languages:
        different_popularity = input("Enter how popular the language is now: ")
        identified_popularity = list_programming_languages.index(language)
        list_popularity[identified_popularity] = different_popularity

    else:
        pass


    return list_popularity

def print_popular_language(languages:list,popularity:list):
    """this function takes both the languages and how popular they are 
       and returns the most popular language 

       param: languages (list): list of programming languages
              poplarity (list): the status of each languages popularity

        returns: high_language (list): the names of the most popular languages

    """

    high_language = []
    for i,status in enumerate(popularity):
        if status == 'High':
            high_language.append(languages[i])
        else:
            pass

    print(f"The most popular langauges are currently: \n")
    for i,languages in enumerate(high_language):
        print(f"{(i+1):<15}{languages:<15}\n")


# Output 

def main():
    list_programming_languages = ["Python","Java","C++","JavaScript","Ruby"]
    list_popularity = ["High","High","Medium","High","Low"]
    language = get_non_empty_string("Enter a programming language: ")
    update_popularity(language,list_programming_languages,list_popularity)
    print_popular_language(list_programming_languages,list_popularity)
    print_languages_and_popularity(list_programming_languages,list_popularity)

if __name__ == "__main__":
    main()


