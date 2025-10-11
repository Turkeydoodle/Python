print('rock paper sissors game')
p1 = input('who is player 1?')
print(f'{p1} will be player 1.')
p2 = input('who is player 2?')
print(f'{p2} will be player 2.')
print('here are the rules: g is sissors, f is rock and h is paper. memorize where they are. you will not need yo see.')
print('close your eyes and position them so you can hit them.')
aa = input('player 1, your turn.')
ab = input('player 2, your turn.')
if aa == ab:
    print('tie!')
if aa == 'F' and ab == 'H':
    print('player 2 wins!')
if aa == 'H' and ab == 'F':
    print('player 1 wins!')
if aa == 'G' and ab == 'H':
    print('player 1 wins!')
if aa == 'H' and ab == 'G':
    print('player 2 wins!')
if aa == 'F' and ab == 'G':
    print('player 1 wins!')
if aa == 'G' and ab == 'F':
    print('player 2 wins!')