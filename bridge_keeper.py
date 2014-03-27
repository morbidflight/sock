question1 = 'What is your name?'
question2 = 'What is your quest?'
question3 = 'What is your favorite color?'

answer1 = ''  # 'Tell me your name.'
answer2 = ''  # 'Tell me your quest.'
answer3 = ''  # 'Tell me your favorite color'

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

color_error = "I\'m sorry, that is not a color of the rainbow."


answer1 = raw_input(question1)
#print(answer1)
answer2 = raw_input(question2)
print("That's a silly quest. Moving on.")
answer3 = raw_input(question3)
while answer3 not in colors:
    print(color_error)
    answer3 = raw_input(question3)
print("You may pass.")
