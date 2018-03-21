#Vamshi Adimulam 903161218
#vamshi.adimulam@gatech.edu
#I worked on this assignment alone, using only this semester's course materials.


def cocaCola():
    drink = input("How many cans of Coke did you drink this week?")
    drinkint = int(drink)
    totalAmount = drinkint*0.99
    return totalAmount
   
def parksAndRec():
    weeks =  input("How many do you have to watch Parks and Rec?")
    weeks = int(weeks)
    hours = input("How many hours of TV do you watch a day?")
    hours = float(hours)
    numOfEpisodes = (60*7*weeks*hours)//21
    numOfEpisodes = int(numOfEpisodes)
    return numOfEpisodes
    
def iLoveFrozen(dollars):
    dollars  = float (dollars)
    whatTheatre = input("Which movie theatre will you be going to? Regal, AMC, or SMG?")
    if whatTheatre == "Regal" :
            numWatch = dollars//12
            numWatch = int(numWatch)
            print ("You can watch Frozen" , numWatch, "times.")
    if whatTheatre == "AMC" :
        numWatch = dollars//15
        numWatch = int(numWatch)
        print ("You can watch Frozen" , numWatch, "times.")
    if whatTheatre == "SMG":
        numWatch = dollars//15
        numWatch = int(numWatch)
        print ("You can watch Frozen" , numwatch, "times.")  
        
def oscars(winners):
    winners = int (winners)
    howLong = input ("How much time does each person have fo their speech? (In minutes)?")
    howLong = int (howLong)
    length = winners*howLong
    hours = length//60
    minutes = length%60
    endingHours = hours + 8
    endingTime = print ("The Oscars will end at" , str(endingHours)+ ":" + str(minutes) + ".")
    
def springBreakCalc(people, miles, costOfHotel):
    people = int(people)
    miles = float (miles)
    costOfHotel = float (costOfHotel)
    MPG = input("What's your MPG?")
    costOfGas = input ("What's the cost of gas?")
    pertip = input("What percentage of tip do you want to add to the hotel bill?")
    MPG = float(MPG)
    costOfGas = float (costOfGas)
    pertip = float (pertip)
    totalCost = ((miles/MPG)*costOfGas)+(1+(pertip/100))*costOfHotel
    costPer = totalCost/people
    rounded = round(costPer,2)
    howMuchPay = print("Each person needs to pay $" + str(rounded) , "this Spring Break.")
    
def breakfastPlatters(eggs,bacon,grit):
    numEggs = eggs//2
    numBacon = bacon//3
    numGrit = grit//1
    
    numOfPlatters = sorted([numEggs, numBacon, numGrit])
    return numOfPlatters[0]    