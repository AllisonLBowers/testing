def starting_question(starting_text, ending_text="You have rejected the wisdom of the ancients. Goodbye!"):
	var = raw_input(starting_text).lower()
	if var == "y" or var == "yes":
		pick_color("Please select a color. Your choices are Blue, Green, Red, and Yellow: ")
	elif var == "n" or var == "no":
		print ending_text
	else:
		starting_question("Invalid response. Please type Y or N: ", ending_text)

def print_letters(b):
	for a in b:
		print a

def pick_color(question):
	var = raw_input(question).lower()
	if var == "blue" or var == "yellow":
		print_letters(var)
		color_blue("You see the numbers 1, 2, 5, and 6. Please select a number: ")
	elif var == "green" or var == "red":
		print_letters(var)
		color_green("You see the numbers 3, 4, 7, and 8. Please select a number: ")
	else:
		pick_color("Invalid response. Please type in Blue, Green, Red, or Yellow: ")


def color_blue(question): 
	text = "The fortune teller moves {} {}. You see the numbers {}, {}, {}, and {}. Choose carefully to receive your fortune: "
	var = raw_input(question)
	if var == "1":
		number_set2(text.format("1", "time", "3", "4", "7", "8"))
	elif var == "2":
		number_set1(text.format("2", "times", "1", "2", "5", "6"))
	elif var == "5":
		number_set2(text.format("5", "times", "3", "4", "7", "8"))
	elif var == "6":
		number_set1(text.format("6", "times", "1", "2", "5", "6"))
	else:
		color_blue("Invalid response. Please select number 1, 2, 5, or 6: ")

def color_green(question):
	text = "The fortune teller moves {} {}. You see the numbers {}, {}, {}, and {}. Choose carefully to receive your fortune: "
	var = raw_input(question)
	if var == "3":
		number_set1(text.format("3", "times", "1", "2", "5", "6"))
	elif var == "4":
		number_set2(text.format("4", "times", "3", "4", "7", "8"))
	elif var == "7":
		number_set1(text.format("7", "times", "1", "2", "5", "6"))
	elif var == "8":
		number_set2(text.format("8", "times", "3", "4", "7", "8"))
	else:
		color_green("Invalid response. Please select number 3, 4, 7, or 8: ")

def number_set1(question):
	var = raw_input(question)
	if var == "1":
		print "Pay attention to your dreams. You will have a vision that leads to great success!"
	elif var == "2":
		print "You will meet a stranger in need of help. Lend your assistance and you will be greatly rewarded!"
	elif var == "5":
		print "A long-forgotten childhood dream will soon be remembered."
	elif var == "6":
		print "A new creative opportunity will present itself in the coming months."
	else:
		number_set1("Invalid response. Please select number 1, 2, 5, or 6: ")
     	print "~*~*~*~*~"
     	print ""
	starting_question("Would you like to play again? Y/N: ", "Thanks for playing!")

def number_set2(question):
	var = raw_input(question)
	if var == "3":
		print "You will receive important advice from an unexpected source. Be sure to follow it."
	elif var == "4":
		print "You will discover a new passion or talent in the coming year."
	elif var == "7":
		print "You will be faced with an important decision that will help realize your true potential."
	elif var == "8":
		print "You are about to receive an unexpected gift, but if you're not looking, you might miss it."
	else:
		number_set2("Invalid response. Please select number 3, 4, 7, or 8: ")
        print "~*~*~*~*~"
     	print ""
	starting_question("Would you like to play again? Y/N: ", "Thanks for playing!")

starting_question("Welcome to the Fortune Teller! Would you like to know your future? Y/N: ")
