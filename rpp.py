import os, random

pad = "    "
quitStrings = ["exit", "quit", "q"]
kill = False
response = None
mode = 'rps'
modes = ('rps', 'rpsls')

rulesRPS = [
    ('rock', 'crushes', 'scissors'),
    ('paper', 'covers', 'rock'),
    ('scissors', 'cuts', 'paper')
]

rulesRPSLS = [
    ('rock', 'crushes', 'scissors'),
    ('paper', 'covers', 'rock'),
    ('scissors', 'cuts', 'paper'),
    ('lizard', 'poisons', 'spock'),
    ('spock', 'smashes', 'scissors'),
    ('rock', 'crushes', 'lizard'),
    ('scissors', 'decapitates', 'lizard'),
    ('lizard', 'eats', 'paper'),
    ('paper', 'disproves', 'spock'),
    ('spock', 'vaporizes', 'rock')
]

def paddedPrint(message):
    print (pad + message)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def printTitle():
    cls()
    print ("""\
    
    
    8888888b.                   888               8888888b.                                                   888            
    888   Y88b                  888               888   Y88b                                                  888            
    888    888                  888               888    888                                                  888            
    888   d88P .d88b.   .d8888b 888  888          888   d88P 8888b.  88888b.   .d88b.  888d888        .d88b.  888888 .d8888b 
    8888888P" d88""88b d88P"    888 .88P          8888888P"     "88b 888 "88b d8P  Y8b 888P"         d8P  Y8b 888   d88P"    
    888 T88b  888  888 888      888888K           888       .d888888 888  888 88888888 888           88888888 888   888      
    888  T88b Y88..88P Y88b.    888 "88b d8b      888       888  888 888 d88P Y8b.     888  d8b      Y8b.     Y88b. Y88b.    
    888   T88b "Y88P"   "Y8888P 888  888 88P      888       "Y888888 88888P"   "Y8888  888  88P       "Y8888   "Y888 "Y8888P 
                                         8P                          888                    8P                               
                                         "                           888                    "                                
                                                                     888
                                                                                                                         
    """)

def inputToLower():
    return str.lower(input(pad))
    
def printResults():
    paddedPrint("You chose '" + response + "'")
    if computerMove:
        paddedPrint("The computer chose '" + computerMove + ".'")
        
    print ('')
    
def getValidMoves(rules):
    validMoves = []
    for (x, y, z) in rules:
        if x not in validMoves:
            validMoves.append(x)
            
    return validMoves
    
def printPrompt():
    if mode == 'rps':
        paddedPrint("You are playing 'Rock, Paper, Scissors.'")
    elif mode == 'rpsls':
        paddedPrint("You are playing 'Rock, Paper, Scissors, Lizard, Spock.'")
    else:
        paddedPrint("I'm not sure what you're doing.")
        
    paddedPrint("Please enter your move, or 'mode' to switch modes.")
    
def switchModes(currentMode):
    newMode = None
    newValidMoves = None
    newRules = None
    
    if currentMode == 'rps':
        newMode = 'rpsls'
        newRules = rulesRPSLS
    else:
        newMode = 'rps'
        newRules = rulesRPS
        
    newValidMoves = getValidMoves(newRules)
        
    return (newMode, newValidMoves, newRules)
    
def getMatchResults(resp, comp, rules):
    if resp == comp:
        return (None, None)
    
    for rule in rules:
        victor, v, loser = rule
        if resp == victor and comp == loser:
            return ("player", v)
        elif resp == loser and comp == victor:
            return ("computer", v)
    
# INIT
currentRules = rulesRPS
validMoves = getValidMoves(currentRules)
winner = None
verb = None
results = None
scores = dict({"player": 0, "computer": 0, "draws": 0})
matchList = []
matchId = 0
    
def validateInput(input):
    valid = False
    
    if input in quitStrings:
        valid = True
    elif input in validMoves:
        valid = True
        
    if input == "mode":
        valid = True
        
    return valid 

# START
while not kill:
    printTitle()
    
    if response and response != "mode":
        printResults()

    if results:
        paddedPrint(results)
    
    printPrompt()
    
    response = inputToLower()
    while not validateInput(response):
        printTitle()
        paddedPrint("'" + response + "'" + " is not a valid move or command.  Please try again.\n")
        printPrompt()
        response = inputToLower()
        
    if response in quitStrings:
        kill = True
        printTitle()
        paddedPrint("I ALREADY MISS YOU.\n")
        break
        
    if response == "mode":
        results = None
        mode, validMoves, currentRules = switchModes(mode)
    else:
        computerMove = random.choice(validMoves)
        winner, verb = getMatchResults(response, computerMove, currentRules)
        
        if not winner:
            results = "Both picked '" + response + ",' so it was a draw!!!"
            scores["draws"] += 1
        elif winner == "player":
            results = "You won, " + response + " " + verb + " " + computerMove + "!!!"
            scores["player"] += 1
            if mode == "rpsls" and response == "rock" and computerMove == "scissors":
                results = results + " (... as it always has)"
        else:
            results = "You lost, " + computerMove + " " + verb + " " + response + "!!!"
            scores["computer"] += 1
            if mode == "rpsls" and computerMove == "rock" and response == "scissors":
                results = results + " (... as it always has)"
            
        matchId += 1