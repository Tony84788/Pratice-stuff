import random as ra

def play():
    user = input('r for rock, p for paper, s for scissors: ').lower()
    computer = ra.choice(['r', 'p', 's'])

    print("user: ", user)
    print("computer: ", computer)

    if user == computer:
        return "It\'s a tie"

    wins = {
        ('r', 's'),
        ('p', 'r'),
        ('s', 'p')
    }
        
    if (user, computer) in wins:
        return 'You won'
    else:
        return "You lost"

print(play())
