print('-'*65)
print('Morbid Predictions Program:')
print()
print('Description: This program asks you for your current age and tells you the year that you will die (on average). ')
print()
age = input('What is your age today? ')
age = int(age)
print('...thinking...')
print('...thinking...')
print('...thinking...')
yearsleft = 79 - age
answer = 2018 + yearsleft
answer = str(answer)
print('You will die in the year...' + answer + '.')
print('-' * 65)