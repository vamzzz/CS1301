# Vamshi Adimulam
#GTID 903161218
#vamshi.adimulam@gatech.edu
# I worked on this assignment alone, using only this semester's resources.

from Myro import *


def firstEvent():
    motors(.5,3,13.3)
    stop()
    for t in timer(13.3):
        if getIR() == [1,1]:
            motors(.5,3,13.3)    
        
def secondEvent():
    center = getObstacle(1)
    for t in timer(15):
        if center > 5000:
            beep(0.5,800)
            motors(-1,-1,.2)
        
def celebration():
    motors(0,3,3)
    motors(-1,-1,1)
    motors(3,0,3)
    motors(1,1,1)
    motors(-1,3,2)
    motors(-1,-1,3)
    motors(.5,2.5,2.5)
    
           
def victoryLap():
    for i in range(0,3):
        beep(.5,600)
        beep(.5,700)
        beep(.5,800)
        beep(.5,900)
        beep(.5,1000)
        beep(.5,1100)
        beep(.5,1000)
        beep(.5,900)
        beep(.5,800)
        beep(.5,700)
        beep(.5,600)
    celebration()
    

def menu():
    userInput = input ("""
    1 Relay Race
    2 Trap Shooting
    3 Victory
    4 Exit
    Which option would you like?""")
    return userInput

def olympicsMenu():
    aList= []
    num = [1,2,3]
    myfile = open("replay.txt","w")
    x = True
    userInput = int(input("""
        1 Relay Race
        2 Trap Shooting
        3 Victory
        4 Exit
        Which option would you like?"""))
    while userInput in num:
        if userInput == 1:
            firstEvent()
            aList.append(userInput)
            userInput = int(input("""
            1 Relay Race
            2 Trap Shooting
            3 Victory
            4 Exit
            Which option would you like?"""))  
        elif userInput == 2:
            secondEvent()
            aList.append(userInput)
            userInput = int(input("""
            1 Relay Race
            2 Trap Shooting
            3 Victory
            4 Exit
            Which option would you like?"""))
            
        elif userInput == 3:
            victoryLap()
            aList.append(userInput)
            userInput = int(input("""
            1 Relay Race
            2 Trap Shooting
            3 Victory
            4 Exit
            Which option would you like?"""))
    while userInput not in num:
        if userInput == 4:
            aList.append(userInput)
            break
        else:
            print("I'm sorry that is not a valid choice")
            userInput = int(input("""
            1 Relay Race
            2 Trap shooting
            3 Victory
            4 Exit
            Which option would you like?"""))
    print("Great work!")
    for i in aList:
        if i == 1:
            print("Your robot won the Relay Race!")
        if i == 2:
            print("Your robot won Trap Shooting competition!")
        if i == 3:
            print("Your robot won a Gold Medal and celebrates the victory!")
    myfile = open("replay.txt","w")
    for i in aList:
        replay.write(str(x) + "\n")
    replay.close()       
        
        
def instantReplay(filename):
    myfile = open(filename,"r")
    reading = myfile.readline()
    for i in reading:
        if i == 1:
            firstEvent()
        elif i == 2:
            secondEvent()
        elif i == 3:
            victoryLap()
    myfile.close()
        
     
    
    
    
            
    