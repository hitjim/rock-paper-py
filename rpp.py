import os

pad = "    "
quitStrings = ["exit", "quit", "q"]

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
    return str.lower(input('    '))
    
def printResults():
    paddedPrint ("You responded " + response)
    
def getValidMoves(rules):
    validMoves = []
    for (x, y, z) in rules:
        if x not in validMoves:
            validMoves.append(x)
            
    return validMoves
        
    
def printPrompt():
    if response and not kill:
        printResults()
    
    paddedPrint ("You are play")
    
# INIT
printTitle()
kill = False
response = None

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

validMoves = getValidMoves(rulesRPS)
    
def validateInput(input):
    valid = False
    
    if input in quitStrings:
        valid = True
    elif input in validMoves:
        valid = True
        
    return valid 

# START
while not kill:
    printTitle()
    printPrompt()
        
    response = inputToLower()
    while not validateInput(response):
        printTitle()
        paddedPrint(response + " is not a valid move or command.  Please try again.")
        response = inputToLower()
        
    if response in quitStrings:
        kill = True
        printTitle()
        paddedPrint ("I ALREADY MISS YOU.\n")