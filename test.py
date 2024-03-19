# Author: Daniel Soden
# Purpose: Github Testing

# Functions


def greet_user(name: str):
    """This function greets a user with their real name

    :param: Name: string referring to a user's name

    :returns: None, just prints
    """
    print(f"Helly {name}, how are your doing?!")


# Main Output


def main():
    user = str(input("What is your name?  "))
    greet_user(name=user)


if __name__ == "__main__":
    main()
