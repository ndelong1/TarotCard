import basic_tarot
import int_tarot
import adv_tarot
from pygame import *


# Select Level:
level = str(input("Beginner, Intermediate, Advanced? "))

x = level.lower


if x == "beginner":
    x == 1
elif x == "intermediate":
    x == 2
elif x == "advanced":
    x == 3
else:
    x == 4


#User did not enter a level (x == 4)
echo = "ERROR. Sorry you did not select a level"


if x == 1:
	
	reading1 = input("What reading style would you like? ('Single card' (1), 'Past, Present, future' (3), 'Celtic Cross' (10), 'New Years' (13)?")
	
	a = int(reading1)
	
	if a == 1:

		print(basic_tarot.Basic(1))

	elif a == 3:

		print(basic_tarot.Basic(3))

	elif a == 10:

		print(basic_tarot.Basic(10))

	elif a == 13:

		print(basic_tarot.Basic(13))

elif x == 2:

	style = input("What reading style would you like? ('Single card' (1), 'Past, Present, future' (3), 'Celtic Cross' (10), 'New Years' (13)?")

	b = int(style)

	if b == 1:

		print(int_tarot.Intermediate(1))
	elif b == 3:

		print(int_tarot.Intermediate(3))

	elif b == 10:

		print(int_tarot.Intermediate(10))

	elif b == 13:

		print(int_tarot.Intermediate(13))

elif x == 3:
	
	code = input("What reading style would you like? ('Single card' (1), 'Past, Present, future' (3), 'Celtic Cross' (10), 'New Years' (13)?")

	c = int(code)

	if c == 1:

		print(adv_tarot.Advanced(1))

	elif c == 3:

		print(adv_tarot.Advanced(3))

	elif c == 10:

		print(adv_tarot.Advanced(10))

	elif c == 13:

		print(adv_tarot.Advanced(13))

else:

	print(echo)

