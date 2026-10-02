from random import shuffle

suits = ['Hearts', 'Diamonds', 'Spade', 'Club']
ranks = ['A','2','3','4','5','6','7','8','9','10','J','K','Q']

card = []
for suit in suits:
    for rank in ranks:
        card.append(f'{suit} of {rank}')

print('Original Deck')
print((card))

shuffle(card)
print('Shuffled Deck')
print(card)
