import random
#Rock-Paper-Scissors
def rockpaperscissors():
	wins=0
	loses=0
	throws = [ "Rock", "Paper", "Scissors" ]
	while True:
		while True:
			playerthrow = input("Chose your weapon. \n [R]ock | [P]aper | [S]cissors \n :")
			if playerthrow.lower() not in ("r","rock","p","paper","s","scissors"):
				print("Please Select a Valid weapon.\n")
				continue 
			else:
				break
		if playerthrow.lower() in ("r","rock"):
			playerthrow="Rock"
		elif playerthrow.lower() in ("p","paper"):
			playerthrow="Paper"
		elif playerthrow.lower() in ("s","scissors"):
			playerthrow="Scissors"
	
		print(f"playerthrow : {playerthrow}\n")
		computerthrow = random.choice(throws)
		print(f"computerthrow : {computerthrow} \n")
	
		if playerthrow == "Rock":
			if computerthrow == "Scissors":
				print("Player chose Rock, Computer chose Scissors.\n")
				print("You Win!!!!\n")
				wins = wins + 1
			elif computerthrow == "Paper":
				print("Player chose Rock, Computer chose Paper.\n")
				print("You Lose!\n")
				loses = loses + 1
			elif computerthrow == "Rock":
				print("You both chose Rock.\n")
				print("Tied\n")
		elif playerthrow == "Paper":
			if computerthrow == "Scissors":
				print("Player chose Paper, Computer chose Scissors.\n")
				print("You Lose!\n")
				loses = loses + 1
			elif computerthrow == "Paper":
				print("You both chose Paper.\n")
				print("Tied\n")
			elif computerthrow == "Rock":
				print("Player Chose Paper, Computer chose Rock.\n")
				print("You Win!!!!\n")
				wins = wins + 1
		elif playerthrow == "Scissors":
			if computerthrow == "Scissors":
				print("You both chose Scissors.\n")
				print("Tied\n")
			elif computerthrow == "Paper":
				print("Player chose Scissors, Computer chose Paper.\n")
				print("You Win!!!\n")
				wins = wins + 1
			elif computerthrow == "Rock":
				print("You chose Scissors, Computer chose Rock\n")
				print("You Lose!\n")
				loses = loses + 1
		else:
			print("Something went wrong.\n")
		print(f"Wins: {wins}\n")
		print(f"Loses: {loses}\n")
		playagain = input("Would you like to play again? (y|n)\n:")
		if playagain.lower() in ("y","yes"):
			continue
		elif playagain.lower() in ("n","no"):
			print("Good Game\n")
			break	
		else:
			print("Invalid Entry, so play again.\n")
			continue
	return wins, loses
	
def guessthenumber():
	wins=0
	loses=0
	while True:
		print("What difficulty Level would you like? ")
		gamedifficulty = input("easy = 1, medium = 2, hard = 3\n(q to quit)\n:")
		if gamedifficulty.isdigit():
			if int(gamedifficulty) not in (1,2,3):
				print("Invalid Entry (Must be 1, 2, or 3)\n")
				continue
			else:
				print(f"gamedifficulty: {gamedifficulty}\n")
		elif gamedifficulty.lower() == "q":
			print("Good Game!")
			return wins, loses
		else:
			print("Invalid Entry (Must be 1, 2, or 3)\n")
			continue
		while True:
			if int(gamedifficulty) == 1:
				numberrange = 11
				printrange = 10
			elif int(gamedifficulty) == 2:
				numberrange = 21
				printrange = 20
			elif int(gamedifficulty) == 3:
				numberrange = 31
				printrange = 30
			computernumber = random.randrange(1,numberrange)
			while True:
				print(f"Guess a number from 1 - {printrange}")
				playerguess = input(":")	
				if playerguess.isdigit():
					if int(playerguess) > int(printrange):
						print(f"Your guess must be between 1 - {printrange}.\nTry Again.")
						continue
					else: 
						if int(playerguess) == int(computernumber):
							print("You Win!\n")
							wins = wins + 1
							break
						elif int(playerguess) < int(computernumber):
							print("To Low!\n")
							loses = loses + 1
						elif int(playerguess) > int(computernumber):
							print("To High!\n")
							loses = loses + 1
						else:
							print("Something went wrong.\n")
							break
					print("Would you like to guess again?\n(y/n)\n")
					answer = input(":")		
					print()
					if answer == "y":
						continue
						print()
					elif answer == "n":
						print()
						break
				else:
					print("Entry Must be a Number. Try again.")
					continue
			print("Would you like to try again?\n(y/n)\n")
			answer = input(":")		
			if answer == "y":
				continue
				print()
			elif answer == "n":
				break
				print()
			else:
				continue		
		print(f"Wins: {wins}\nLoses: {loses}\n")
		break
	return wins, loses



#guessthenumber()
totalwins=0
totalloses=0
while True:
	#Need to have a catch for if they don't input anything into the gamechoose
	print("What game do you want to play? \n")
	print("(Rockpaperscissors = rps) (Guessthenumber = gtn) ")
	gamechoose=input(":")
	if gamechoose.lower() in ("rockpaperscissors","rps"):
		wins, loses = rockpaperscissors()
	elif gamechoose.lower() in ("guessthenumber","gtn"):
		wins, loses = 	guessthenumber()
	else:
		print(f"You had {totalwins} Wins, and {totalloses} Loses.\n")
		print("Later!")
		break
	totalwins += wins
	totalloses += loses
	continue
