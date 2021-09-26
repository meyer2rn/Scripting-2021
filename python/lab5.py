import random
rannumber = random.randint(1, 10)
number_guesses = 0
print('Please guess a number between 1 and 10')
while number_guesses < 5:
    guess = int(input())
    number_guesses += 1
    if guess < rannumber:
        print('Too Low')

    if guess > rannumber:
        print('Too High')

    if guess == rannumber:
        break
if guess == rannumber:        
        print('Good Job. You guessed correctly!')
