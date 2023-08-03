import random

random_number = random.randint(1, 100)

# print(random_number)

game_count = 1

while True:
    try:
        my_number = int(input('Enter a number between 1 and 100 : '))

        if my_number > random_number:
            print('down')
        elif my_number < random_number:
            print('up')
        elif my_number == random_number:
            print(f'Congratulations. You got it in {game_count} tries.')
            break
        
        game_count += 1
    except:
        print('An error has occurred. Please enter a number.')