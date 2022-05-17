import random


def password_generator():
    capital_letter = ["A", "B","C", "D", "F", "G"]
    lower_case = ["a", "b", "c", "d", "f", "g"]
    symbols = ["!", "¡", "$", "&", "/", "(", ")"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    characters = capital_letter + lower_case + symbols + numbers

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = "". join(password)   
    return password 

def run():
    password = password_generator()
    print("You new password is: " + password)



if __name__== "__main__":
    run()