from random import shuffle
import itertools



deck = list(itertools.product(range(1, 10), ['Spade', 'Heart', 'Diamond', 'Club']))

shuffle(deck)

a = input("1, 3, 5?")

b = int(a)

print("You Got:")
for i in range(b):
	print(deck[i][0], "of", deck[i][1])