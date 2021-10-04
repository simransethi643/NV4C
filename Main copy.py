# ============================================================
# Answers
# ============================================================
answers = {
  #Sun
"How many planets are in our solar system?":"EIGHT",
"How many dwarf planets are there?": "SEVEN",
"What is the sun also known as?": "YELLOW DWARF",
"How many moon does sun has?": "0",
"How many seasons does sun has?": "0",
"Approximately every ... years, the sun changes th way it rotates": "11",
"solar winds come from ...": "THE SUN",
"True or False: Is there a planet names Makemake?": "TRUE",

#Mars
"How many earth days does Mars has?": "687 DAYS",
"How many moons does Mars have?": "TWO",
"How many seasons does Mars has?": "FOUR",
"True or False: Mars has same leath if seasons as earth seasons": "FALSE",
"True or False: Mars is made of dust and gas": "TRUE",

#Saturn
"How many rings does Saturn has?": "7",
"How many moons does Saturn has for sure?": "53",
"How many moons does Saturn currently has?": "29",
"True or False: The farther out you go on the Saturn ring, you might be able to see some part of Phoebe moon": "TRUE",
"Can a person live on planet Saturn": "NO",

#Neptune
"What Neptune is known for": "ICE GIANT",
"True or False: Neptune was discovered by doing mathermatical calculations": "TRUE",
"How many moons does Neptune?": "14",
"How many seasons does Neptune has": "4",
"Can a person live on planet Neptune": "NO",

#Pluto
"True or False: Pluto is a dwarf planet?": "TRUE",
"True or False: Is there a planet named Makemake?": "TRUE",
"True or False: Is there a planet named Ceres?": "TRUE",

#Jupiter
"How many rings does Jupiter have?": "4",
"What is Jupiter's atmosphere made out of?": "HYDROGEN AND HELIUM",
"Which planet has a sand storm that has been going on for hundreds of years?": "JUPITER",
"Who was Jupiter named after?" : "THE KING OF THEROMAN GODS",
"How many moons does Jupiter have?": "79",

#Earth's Moon
"Why can't Earth's moon support life as we know it?": "WEAK ATMOSPHERE AND NO LIQUID WATER",
"What is the 5th largest moon out of the 200 known moons in the Solar System?": "EARTHS MOON",
"How long is a year on the moon?": "27 EARTH DAYS",
"How far is the Earth's moon from the planet earth?": "240,000 MILES",

#Mercury
"Which planet is closest to the sun?": "MERCURY",
"Mercury has __ many moons?": "0",
"How many earth days is 1 day on mercury?": "176",
"Mercury is ___ miles away from earth.": "63.51 MILLION",

#Earth� 
"Earth is catagorized as _____ type of planet.": "TERRESTRIAL",
"Which planet so far is the only one with Liquid Water?": "EARTH",
"It takes ___ earth days to orbit the sun.": "365",
"Earth is ______ miles away from the sun": "93 MILLION",



#Venus
"One axis rotation takes about ____ earth days.": "243",
"Venus is ____ miles from the sun." : "67 MILLION",
"What acid are the clouds of Venus made up of?": "SULFURIC",
"What is Venus' atmosphere mostly made up of?": "CARBON DIOXIDE",

#Uranus
"How many moon does Uranus have?": "27",
"Seasons in Uranus last ... earth years.": "21",
"Approximately how far is Uranus is from the sun?" : "1.8 BILLION MILES",
"Uranus takes about ... Earth years to orbit around the sun.": "84",
"Uranus' ... is made up of mostly molecular hydrogen, atomic helium, and a small amount of methane. ": "ATMOSPHERE",
}
questions = list(answers.keys())

# ============================================================
# Code 
# ============================================================
import random

## Setup
print("Hello Welcome to the game")
print('Welcome to the Milky Way Exploration')
print("How many players are participating?(at least 2 players)")
numberOfPlayers = int(input())
if(numberOfPlayers < 1):
  print("There are not enough players to play the game!")
scores = [0] * numberOfPlayers # list of scores
moves = [0] * numberOfPlayers # list of move positions 0 < x < 50
turn = 0 # turn number
names = []
for i in range(numberOfPlayers):
  name = input("please enter player " + str(i + 1) + "'s name: ") # ask for player names
  names.append(name)

print("This is a board game with 50 spaces.")
print("Your objective is to fly around the galaxy and collect as many resoucres as possible while managing your food supply and resources.")
print("Here are the rules.")
print("each player will roll the dice and move according to the number they rolled.") 
print("players will set up pit stops every planet/moon they visit.") 
print("On every space, there will be a question about our galaxy.") 
print("If players answer the question correctly, they will recieve +1 resources. If the players answer the question incorrectly, then they will not earn any resources.")
print("The player who earns the most resources at the end of the 50 space map will win!")
print("Good luck and have fun!")

running = True
while running:
  playerIndex = turn % numberOfPlayers
  name = names[playerIndex]
  print("\n\n===================================")
  print(name + ", it is your turn!")

  # Options
  print("Option 1: Roll the dice")
  print("Option 2: see what position everyone is in")
  print("Option 3: see all of the player's total resources")
  print("Option 4: next turn")
  print("Option 5: Exit")
  skipTurn = False
  choice = 0
  while choice != 1:
    choice = int(input("Please select what option you would like to choose:"))

    if (choice == 1):
      print("Rolling the dice...")
      print("You have rolled a ")
      roll = random.randint(1,6)
      print(roll)
      moves[playerIndex] += roll

    elif choice == 2:
      for i in range(numberOfPlayers):
        print(names[i] + " is on space " + str(moves[i]))

    elif choice == 3:
      for i in range(numberOfPlayers):
        print(names[i] + " has " + str(scores[i]) + " resources")
      leadingIndex = scores.index(max(scores))
      print(names[leadingIndex] + " is in the lead!")

    elif choice == 4:
        skipTurn = True
        break

    elif choice == 5:
      print("Game over, thank you for playing!")
      quit()
  if(skipTurn):
    continue

  # Questions
  q = random.choice(questions)
  a = answers [q]
  print (q)
  user_answer = input().lower()
  if a == user_answer:
    print ("Correct")
    scores[playerIndex] += 1
  else:
    print ("Incorrect")

  turn += 1
print("Congrats! The game is finished")
winnerIndex = scores.index(max(scores))
print("The winner of the game is " + names[winnerIndex] + "!")
print("Thanks for playing!")
quit()