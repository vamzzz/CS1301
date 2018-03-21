#Vamshi Adimulam 903161218
#vamshi.adimulam@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.




def mixtapeFire(timesPlayed,rating):
    if timesPlayed >= 100 and rating >= 3 and rating <= 5:
        return "Your mix tape is fire!"
    elif rating > 5:
        return "Invalid input. Try again."
    else:
        return "You should quit the rap game."
        
        
        
  
def myFaveSong (song,artist):
    count = 1
    song = song.lower()
    while count<6:
    
        if count == 1:
            hint = 0
            guess = input("Guess my favorite song.")
            guess = guess.lower()
            if guess == "hint":
                print ("The artist who wrote the song is:" , artist)
                hint = hint + 1
            if guess == song:
                print ("Great Job! It took you", count, "tries and", hint
                , "hints to guess my favorite song.")
                print ("Thank you for playing!")
                return None
        else:
            guess = input ("Try again. Guess my favorite song.")
            guess = guess.lower()
            tries =0
            hint = "hint"
            if guess == hint:
                print ("The artist who wrote the song is:", artist)
                tries = tries+1
            if guess == song:
                print ("Great Job! It took you,", count, "tries and", tries,
                "hints to guess my favorite song.")
                print ("Thank you for playing!")
                return None 
            else:
                print ("Try again. Guess my favorite song:")
    
        count = count+1
    print("You have exceeded the number of tries.")
    print("Thank you for playing!")
        
                
       
def illuminatiConfirmed (secretMsg):
    count = 0
    for i in str(secretMsg):
        if i == "$":
            count = count + 1
    if count == 3:
        secretMsg = secretMsg.replace("$", "s")
        print(secretMsg)
        print ("Illuminati Confirmed.")
    if count != 3:
        print (secretMsg)
        print ("Probably not Illuminati.") 
            
def decrementNumbers (aString):
    count = 0
    num = input ()
    for i in str(aString):
        if i == num:
            count = count + 1    
    if count == 0: 
        print ("Try a different number.")
        return None
    else:
        newString = aString.replace (num, str(int(num)-1))    
    return newString
        
def numberTie(num): 
    num1 = num
    num2 = num
    a=0
    for i in range (num,0,-1):
        print ((" "*a)+str(num)*(num*2))
        num = num - 1
        a = a+1
        
    b = 1
    for c in range (b, num1 + 1, 1):
        print ((" "*(num1-1))+str(b)*(b*2))  
        num1 = num1 -1
        b = b + 1
        
    d = 0
    for e in range (num2, 0 ,-1):
        print ((" "*d)+ str(num2)*(num2*2))
        num2 = num2 -1
        d = d+1
def countUp (start,limit,increment):
    a = print ((str(range(start, limit + 1, increment))))
  