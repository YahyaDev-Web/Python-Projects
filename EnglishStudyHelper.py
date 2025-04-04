# import important library
import random , time , os

# ask the user about his name

student_name = input("Hello dear student, Please enter your name: ")
print("-"*35)
# print the title of the application
print(f"Welcome 👋 {student_name.title()} to Study Helper 📚.")


# dictionary with the words and definitions 
WORDS = { 
    "Absence": "The lack or unavailability of something or someone.", 
    "Approval": "Having a positive opinion of something or someone.", 
    "Answer": "The response or receipt to a phone call, question, or letter.", 
    "Attention": "Noticing or recognizing something of interest.", 
    "Amount": "A mass or a collection of something", 
    "Borrow": "To take something with the intention of returning it after a period of time.", 
    "Baffle": "An event or thing that is a mystery and confuses.", 
    "Ban": "An act prohibited by social pressure or law.", 
    "Banish": "Expel from the situation, often done officially.", 
    "Banter": "Conversation that is teasing and playful.", 
    "Characteristic": "referring to features that are typical to the person, place, or thing.", 
    "Cars": "Four-wheeled vehicles used for traveling.", 
    "Care": "extra responsibility and attention.", 
    "Chip": "a small and thin piece of a larger item.", 
    "Cease": "to eventually stop existing.", 
    "Dialogue": "A conversation between two or more people.", 
    "Decisive": "a person who can make decisions promptly.", 
}
message = """
1. Review random word 📜
2. Test yourself 🧪
3. Exit 🚪
"""

# this func is for clearing  the console: 
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")






while True:
    
    print(message)
    # global variables
    lst = []
    for word in WORDS:
        lst.append(word)
        random_word = random.choice(lst)
        definition = WORDS[random_word]
    # ask user about his choice
    choice = input("Enter your choice: ")


    # define review section
    def review_a_word():
        print(f"Word: {random_word} \n Definition: {definition}")
        print("⚠ : The word and definition will disappear after 5 sec, be fast ⚡")
        time.sleep(5)
        clear_console()
        print("-"*25)

    # define testing section
    def test_student():
        print(f"Definition: {definition} \n ⚠ : The definition will disappear after 5 sec, be fast ⚡")
        time.sleep(5)
        clear_console()
        print("-"*25)


        count = 3
        while count > 0:
            testing_word = input("Enter the word: ").title()
            if testing_word == random_word:
                print("Correct answer 🥳 , go and review more words champion 🏆 ")
                break
            else:
                count -= 1  
                if count > 0:
                    attempt_word = "attempt" if count == 1 else "attempts"  
                    print(f"Incorrect answer, you have {count} {attempt_word} remaining.")
                else:
                    print("Incorrect answer you have 0 attempts remaining. Better luck next time!")







    # 1 this section will be for reviewing random words
    if choice == "1":
        review_a_word()
    # 2 this section will be for the students that want to test their selfs
    elif choice == "2":
        test_student()
    # 3 this place is when the user wants to quit
    elif choice == "3":
        break
    # this section for expecting a wrong choice of user
    else:
        print("Invalid 🚫 input , please enter a valid choice.")