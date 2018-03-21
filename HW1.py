#Vamshi Adimulam
#Section A1
#GTID: 903161218
#Email: vamshi.adimulam@gatech.edu
#I worked on the homework assignment alone, using only this semester's course materials.

import math

def fluidConversion():
    ouncesInt = 0;
    try:
        ounces = input("What are the number of fluid ounces would you like to convert?")
        ouncesInt = int(ounces)
    except:
        print("Sorry, that's not a valid answer, try again!")
        ouncesInt = fluidConversion()
    return ouncesInt
    
ounces = fluidConversion()
gallons = (ounces//128)
gallonsrem = (ounces%128)
quart = (gallonsrem//32)
quartrem = (gallonsrem%32)
pint = (quartrem//16)
pintrem = (quartrem%16)
gill = (pintrem//4)


print(ounces,"fluid ounces is", gallons, "gallon(s),", quart , "quart(s),", pint, "pint(s), and", gill, "gill(s)")


#Cone volume
import math

def coneVolume():
    radius = input("What is the radius of your cone in feet?")
    radiusInt = int(radius)
    return radiusInt
    

height = input("What is the height of your cone in feet?")
heightInt = int(height)


radius = coneVolume()
volume = ((math.pi*(radius**2)*heightInt)/3)
print("Volume of a cone with a radius of", radius, "and a height of ", height ,"is", volume ,"feet-cubed")

#calorieIntake

def calorieIntake():
    meals = input("How many meals do you eat today?")
    mealsInt = int(meals)
    return mealsInt
    
miles = input("How many miles did you run today?")
milesflo = float(miles)

meals = calorieIntake()

calorieGain = (500*meals)
calorieBurn = (1600+(95*milesflo))
netCalorie = (calorieGain - calorieBurn)

print("After eating" , meals, "meals and running" , miles, "miles, a person gained",
calorieGain, "calories and burned", calorieBurn, "calories, leading to an intake of", 
netCalorie, "calories.")

def paycheckAfterTaxes():
    earnMoney = input("What is the total amount of money do you earn?")
    earnMoneyflo = float(earnMoney) 
    earnMoneyflo = round(earnMoneyflo,2)
    return earnMoneyflo
    
percentTax = input("What percetages of taxes should be taken out of your paycheck?")
percentTaxflo = float(percentTax)
percentTaxflo = round(percentTaxflo,2)

earnMoney = paycheckAfterTaxes()

correctTax = (earnMoney*(1-(percentTaxflo*.01)))
correctTax = round(correctTax,2)

earnMoneyStri = str(earnMoney)
percentTaxStr = str(percentTaxflo)

CorrectTaxStr = str(correctTax)

print("Your corrected paycheck of $"+ earnMoneyStri, "after", percentTax+ "% due to taxes is $"
+CorrectTaxStr+ ".")
