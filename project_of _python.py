quetions = ("Which function is used to display output in Python?",
           "Which symbol is used for comments in Python?",
           "What is the output of print(5 + 3)?",
           "Which data type stores True or False values?",
           "Which loop is used to repeat code while a condition is true?",
           "Which of the following are valid Python data types? Select all correct answers.")


options = (("A.input()","B.display()","C.print()","D.show()"),
          ("A.//","B.#","C/* */","D.@"),
          ("A.6","B.5","C.8","D.7"),
          ("A.float","B.bool","C.int","D.complex"),
          ("A.while","B.for","C.do-while","D.def"),
          ("A.str","B.number","C.float","D.int"))

answers = ("C", "B", "C", "B", "A", "A")

gusess = []
score = 0
quetion_num = 0

for quetion in quetions:
    print("--------------------")
    print(quetion)
    for option in options[quetion_num]:
        print(option)
    guse = input("enter A,B,C,D ").upper()
    gusess.append(guse)
    if guse == answers[quetion_num]:
        score += 1
        print("correct")
    else:
        print("incorrect")
        print(f"{answers[quetion_num]} is the correct answer ")

    quetion_num += 1




print("****************************")
print("         RESULT             ")
print("****************************") 


print("answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("geuses: ",end="")
for gese in gusess:
    print(answer, end=" ")
print()


score = int(score / len(quetions) * 100)
print(f"your score is: {score}%")



