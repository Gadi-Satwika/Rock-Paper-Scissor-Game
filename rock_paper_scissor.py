#Importing Modules
import random
import emoji

#Initializing Each Scores
user_score = 0
computer_score = 0
Tie = 0

#Performing Rock_Paper_Scissor Game Based on User and Computer Inputs
def check_win(computer,user):
	#Calling Global Variables to make changes
	global user_score
	global computer_score
	global Tie
	#Check winners based on the Game conditions
	if( computer == user ):
		print(laughing," It's a Tie!") #Printing for the users
		Tie+=1 #Calculating Tie Score
		return "Tie!" #Here Returning Value to append into History
	elif( (user== rock and computer == scissor) ):
		print(random.choice(win_reactions)) #To get random reactions from the given win_reactions list
		user_score+=1
		return "You Win!"
	elif(  (user == paper and computer == rock) ):
		print(random.choice(win_reactions))
		user_score+=1
		return "You Win!"
	elif( (user ==  scissor and computer == paper) ):
		print(random.choice(win_reactions))
		user_score+=1
		return "You Win!"
	else:
	 	print(random.choice(lost_reactions))
	 	computer_score+=1
	 	return "You Lost!"
	 	print()

#Initializing all emojis needed for this page
rock = emoji.emojize(":rock:",language = 'alias')
paper = emoji.emojize(":scroll:",language = 'alias')
scissor = emoji.emojize(":scissors:",language = 'alias')
laughing = emoji.emojize(":joy:",language = 'alias')

win1 = emoji.emojize(":partying_face:",language = 'alias' )
win2 = emoji.emojize(":tada:",language = 'alias')
win3 = emoji.emojize(":confetti_ball:",language = 'alias')
win4 = emoji.emojize(":fire:",language='alias')

win_reactions = [ win1 +"Yay! You Won The Game" ,
win2+" Congrats! You Crushed It ",
win3+" Victory dance time!",
win4+"You're on Fire"
]

lost1 = emoji.emojize(":cry:",language = 'alias')
lost2 = emoji.emojize(":pensive:",language = 'alias')
lost3 = emoji.emojize(":worried:",language = 'alias')

lost_reactions = [lost1+"You Lost! Try Again",
lost2+"Oops! Better Luck Next Time",
lost3+" Sad, Play Again!"
]

#List where the computer should select random one from this list
options = [ rock,paper,scissor ]

print("Play the Game")
#To Display in the output for users
print("1:  Rock"+ rock)
print("2:  Paper"+paper)
print("3:  Scissor"+scissor)
print()
#Storing History in List
history_store = []
#Game Functions to take inputs from user and computer, performing check_win functions , appending the data into history, Printing Score
#Asking user whether to play again or not? (Infinity times they can play the game
def play_the_game():
	computer = options[random.randint(0,2)]
	input_user =  int(input("Enter Your Choice: [1,2 or 3] : "))
	if input_user<=3:
		user = options[input_user-1]
		print("\nYou:", user)
		print("Computer:", computer)
		who_wins = check_win(computer, user)
		history_add = "Your choice:"+user +"| Computer Choice:"+computer + " *---* "+who_wins
		history_store.append(history_add)
		play_again = input("\nDo You Want To Play Again:(y/n):  ")	
		if play_again=='y':
			play_the_game()
		else:	
			print("\nyour Score: ",user_score)
			print("computer Score: ",computer_score)
			print("Tie: ",Tie)
			print("\nGame History: ")
			for eachtime in history_store:
				print(eachtime)
	else:
		print("Invalid Choice")
		play_the_game()
#To start the code or to start the game, Calling the game.

play_the_game()

