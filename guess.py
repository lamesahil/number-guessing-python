import random
def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print('Guess The Number Between 1 to 100')
    
    while attempts<5:
        guess = int(input('Your Guess: '))
        attempts += 1
        
    
        if guess == number:
            print(f"Correct! You guessed it in {attempts} tries. ")
            return 100 - (attempts*15)
        elif guess < number:
            print("Too Low")
        else:
            print('Too High!')
    print(f'Out of attempts! The number was {number}')
    return 0
score = 0
while True:
    score += play_game()
    again = input('Play Again! (y/n): ')
    if again.lower() != 'y':
        break
print(f"Final Score {score}")
