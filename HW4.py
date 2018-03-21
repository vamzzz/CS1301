#Vamshi Adimulam and Anjani Ganapathi
#903161218
#vamshi.adimulam@gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials.


def youAndThe6th(intlist):
    finalList = []
    for i in intlist:
        if i%6 == 0:
            finalList.append(i)
    return finalList
    
def union(list1,list2):
    finalList = []
    finalList = list1+list2
    finalList.sort()
    final2List = []
    for i in finalList:
        if i not in final2List:
            final2List.append(i)        
    return final2List
    
def sentenceGenerator(list1):
    sentence = ""
    for i in list1:
        if type(i) == str : 
            sentence = sentence + " " + i
    if sentence == "" :
        print ("No strings from inputted list.")
        return None  
    print (sentence)
   
def powerLevel (list1):
    power = 1
    for i in list1:
        power = power * i
    power = power + 3000
    if power < 9000:
        print ("Goku needs to increase his power-level by" , str(9000 - power) + "!")
    if power >= 9000:
        print ("It's over 9000!")
               
def multiplyNums(aList):
    total = 1
    count = 0
    for i in aList:
        if type(i) == int or type(i) == float:
            total = total * i
            count = count + 1
        if type(i) == list:
            a = multiplyNums(i)
            total = total * a
    if count == 0:
        pass
    return total 


def backwards(string):
    if string == "":
        return string
    else:
        return backwards(string[1:]) + string[0]
        
def abbreviator(s):
    final = ""
    for i in s:
        char = i
        if char.isalpha() == True and char.isupper() == True:
            final = final + char
        if char.isdigit() == True:
            final = final + char
    return final
    
## def evenOdd(aList):
##     pos = 0
##     
##     final = ""
##     for i in aList:
##         if type(i) == str:
##             if pos % 2 == 0:
##                 count = 0
##                 for j in i:
##                     if count < 1:
##                         j = j.lower()
##                         if j == "a" or j == "e" or j== "i" or j == "o" or j == "u":
##                             final = final + j
##                             count = count + 1
##                             print("HI")
##                 
##             if pos % 2 == 1:
##                 count = 0
##                 for j in i:
##                     while count < 1:
##                         j = j.lower()
##                         if j != "a" and j != "e" and j != "i" and j != "o" and j != "u":
##                             final = final + j
##                             count = count +1
##                             print("hi")
##         pos = pos + 1
##     return final

def evenOdd(listA):
    final = ''

    for pos in range(len(listA)):
        count = 0
        if type(listA[pos]) == str:            
            if pos % 2 == 0:
                for j in listA[pos]:
                    if count < 1:
                        j = j.lower()
                        if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
                            final = final + j
                            count = count + 1
                                
            if pos % 2 == 1:
                for j in listA[pos]:
                    if count < 1:
                        j = j.lower()
                        if j != "a" and j != "e" and j != "i" and j != "o" and j != "u":
                            final = final + j
                            count = count + 1
    return final
                      
def parse (aList, delimiter):
    element = ""
    final = []
    for i in aList:
        if i != delimiter:
            element = element + i
        else:
            final.append(element)
            element = ""
    final.append(element)
    return final
            
             
            
            
        
            
    

       

