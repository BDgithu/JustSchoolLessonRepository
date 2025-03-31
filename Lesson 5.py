print("Greetings. Quiz game")

questions = [["Capital of Japan ", "Tokio"]]

score = 0

for question in questions:
    user_answer = input(question[0]).capitalize()
    if user_answer == question[1]:
        print("Congratulations it is true")
        score += 1
    else:
        print("Wrong. Try again")

print(f"Your score is {score}")

