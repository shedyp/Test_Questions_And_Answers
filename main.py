from Questions import Questions

question_prompt = [
    "What color is an apple?\n (a) red/green\n (b) Orange\n (c) purple\n\n",
    "What is color of Nigeria Flag?\n (a) Blue\n (b) Yellow\n (c) Green/White\n\n",
    "What is the continent of Nigeria?\n (a) Africa\n (b) France\n (c) USA\n\n"
]

questions = {
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "c"),
    Questions(question_prompt[2], "a"),
}


def run_test(questions_all):
    score = 0
    for question in questions_all:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
