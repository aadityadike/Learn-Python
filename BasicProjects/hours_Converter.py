# By this Program you can convert days into hours.

def converter(user_input, hours):
    return f"{user_input} days are {user_input * hours} hours."


def check_input(user_input):
    if user_input.isdigit():
        super = int(user_input)
        if super == 0:
            return "0 is not a valid number please enter valid number"
        else:
            return super
    else:
        return "please enter valid number"


def main():
    Hours = 24
    while True:
        user = input(
            "Enter the number of days you want to convert in hours : \n")
        user_input = check_input(user)
        if type(user_input) is str:
            print(user_input)
        else:
            print(converter(user_input, Hours))
            break


main()
