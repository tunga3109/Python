from survey import AnonymousSurvey


# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = 'What is your favorite sport?'
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Sport: ")
    if response == 'q':
        break
    my_survey.add_response(response)


print("\nThank you to everyone who participated in the survey!")
my_survey.show_response()