import random, sys, os
from time import sleep



DEBUG = True

# =======================
# Printing Functions
# =======================

def wait(delay):
    if not DEBUG:
        sleep(delay)

def typingPrint(text, delay=0.02): # Typewriter-like text output function
    effective_delay = 0 if DEBUG else delay
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(effective_delay)

def typingInput(text, delay=0.02): # Typewriter-like input questioning (equivalent to print(" "))
    effective_delay = 0 if DEBUG else delay
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(effective_delay)
    return input()
        
def slowPrint(text): # Slower text output for dramatic effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.06)
        
def slowerPrint(text): # Even slower text output for even more dramatic effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.08)
        
# =======================
# Dialogue / Story
# =======================

dialogue = {1 : 'You wake up in Herschel Car Park in Slough. Getting up, you\'re surrounded by cars of various makes,\n primarily Vauxhalls. You notice inscriptions of G->6 on the walls.\n',
            2 : 'In front of you is a car. The passenger window is down and the door seemingly unlocked.\n To your left is an exit sign and a doorway, and to your right is a stairway leading upwards.\n',
            3 : 'What do you do? Try to drive the car, walk through the exit, or go up the stairs?\n Commands available: go car, go exit, go stairs\n',
            
            4 : '\n			GAME	OVER\nYou try to start the car. Suddenly, you hear shouting. A policeman opens the door.\nYou\'re nicked.\n',
            
            5 : 'You go up the stairs...\n',
            6 : 'You continue up the stairs.\n',
            7 : 'As you walk up the stairs, you notice the chips of paint off the surface of the steps.\n',
            8 : 'The sound of your shoes echo in the room as you continue up the stairs.\n',
            9 : 'A dull grey sheen glimmers faintly on the surface, as you continue up the stairs. The steps beckon for the contact of your shoes.\n',
            10 : 'The harsh incandescent lights buzz incessantly above you. Still, you take step after step after step...\n',
            
            11 : 'You make your way out of the car park, exiting through the doorway onto Buckingham Garden Street.\n',
            12 : 'To your left, the narrow road seems to come to a junction. To your right, the road leads to a mysterious house of sogome kind.\n',
            13 : 'What do you do? Gather your bearings at the junction or try your luck with the house?\n Commands available: go junction, go house\n',
            
            14 : 'Walking up to the house, you suddenly hear faint shouts. On closer inspection you witness an empty bottle of mayonnaise fly out the window,\npassing you.',
            15 : '\nA woman, around the age of 52, walks out of the house, and stares you in the eye.\n',
            16 : '"You there. Could you do me a favour?\n"',
            17 : 'You nod apprehensively.\n',
            18 : 'The woman\'s complexion eases a little. \n"Good. I need a new bottle of Heinz Mayonnaise, and I\'d like you to get it for me from the Tesco across the road."\n',
            19 : 'Do you accept? Commands available: yes, no\n',
            
            20 : 'You shake your head. The woman\'s eyebrows raise in surprise before turning to anger.\n',
            21 : '"Why did I even ask you in the first place? GET OFF MY GARDEN!"\n',
            22 : 'As you begin to stumble hurriedly away, the front door opens once more and you hear the familiar sound of a ketchup bottle being aggressively shaken.\n',
            23 : 'Before you can even look back the bottle strikes your cranium, knocking you out instantly.\n',
            24 : '\n		GAME	OVER\nThe citizens of Slough require mayonnaise as important sustenance - don\'t mess around with it!\n',
            
            25 : 'You walk steadily over to the collection of traffic lights, avoiding cars parked on double yellows and puddles of unknown substances.\n',
            26 : 'As you cross the main road, you see signs pointing to Tesco, Travelodge and WeBuyScrapMetal™.\n',
            27 : 'What do you do? Gather supplies in Tesco, look for a bed in the Travelodge or sell scrap metal?\n Commands available: go tesco, go travelodge, go scrap metal\n',
            
            28 : 'Travelodge',
            29 : 'Scrap metal',
            30 : 'You nod in agreement. The woman sends you off back towards the junction.\n',
            
            31 : 'You walk in to the Tesco. ',
            32 : '\nEntering, you see rows of aisles in front of you. Direction signs hang on the ceiling above, though too far for you to make out clearly.'
            
            
            
    }
def Stair_Loop(progress):
    if progress == 5:
        stairInput = typingInput('Would you like to continue going up the stairs? \n')
        if stairInput.lower().strip() == 'no':
            typingPrint('Wow, quitting so soon? You have no devotion to a cause so you return to where you started. SMH\n')
            progress = 3   
        elif stairInput.lower().strip() == 'yes':
            progress += 1
    elif progress in {6,7,8,9} :
        stairInput = typingInput('Would you like to continue? \n')
        if stairInput.lower().strip() == 'no':
            typingPrint('You decide to cut your losses and return to where you started.\n')
            progress = 3    
        elif stairInput.lower().strip() == 'yes':
            progress += 1     
    elif progress == 10:
        stairInput = typingInput('Would you like to continue? \n')
        if stairInput.lower().strip() == 'yes':
            typingPrint('''In the corners of your eyes the walls seemingly disintegrate to black, but you pay no
attention. You continue up the stairs…
You collapsed.
                    GAME		 OVER
They say insanity is doing the same thing over and over again, expecting a different result…
GGs''')
            progress = 0
        elif stairInput.lower().strip() == 'no':
            slowPrint('.......')
            wait(2)
            typingPrint(' You step out.')
            wait(2)
            typingPrint('\nYou feel a gentle breeze, and looking above you shows a grey overcast sky.')
            wait(2)
            slowPrint('\nYou\'ve made it to the top flo-')
            wait(5)
            slowerPrint('\nCRAAAAAAAASH!')
            wait(4)
            typingPrint('\nYou\'re hit by an inconspicous Honda Accord, trying to park in the spot you walked onto.')
            wait(3)
            slowPrint('\nEND')
            progress = 0
    return progress
# =======================
# Game Flow / Options
# =======================

deathPoints = [4,24]
checkPoints = [3]
savePoints = []
options = {
    3: {"go car": 4, "go stairs": 5, "go exit": 11}, # Car park choice
    13: {"go junction": 25, "go house": 14}, # After taking exit
    19: {"yes": 30, "no": 20}, # Accept tesco quest?
    27: {"go tesco" : 31, "go travelodge" : 29, "go scrap metal" : 30} # junction (can also be after accepting tesco quest)
}
choicePoints = set(options.keys())
days = 1
stairCount = 0

# =======================
# Input Handling
# =======================

def inputCommand():
    userInput = typingInput("\nMake your choice: ")
    return userInput
    
def Check_Input(userIn, p):
    if userIn.lower() == "check days":
        typingPrint(f"You are on day {days}\n")
        return p
    elif userIn.lower().strip() in options.get(p, {}):
        return options[p][userIn]
    else:
        typingPrint("Invalid command. Try again.\n")
        return p


# =======================
# Main Game Loop
# =======================
def main():
    progress = 1
    while progress != -1:
        wait(0.5)
        if progress == 0:
            reset = typingInput('Restart at last save point? yes/no\n')
            if reset.lower().strip() == 'yes':
                progress = savePoints[-1]
                typingPrint('returning to save point......\n')
                os.system('cls')
                wait(2)
            else:
                progress = -1
        typingPrint(dialogue[progress])
        if progress in checkPoints:
            savePoints.append(progress)
        if progress in choicePoints:
            userIn = inputCommand()
            newProgress = Check_Input(userIn, progress)
            progress = newProgress
        elif progress in deathPoints:
            typingPrint('GGs\n')
            progress = 0
        elif progress in {5,6,7,8,9,10}:
            progress = Stair_Loop(progress)
        else:
            progress += 1
    
            
main()




