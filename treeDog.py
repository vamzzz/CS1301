import Graphics
from Myro import *
from Graphics import *

win = Window("My Dog", 500,500)

background = Rectangle((00,00),(500,500))
background.draw(win)
background.fill = makeColor("cyan")

grass = Rectangle((0,220),(500,500))
grass.draw(win)
grass.fill = makeColor("green")

backFoot2 = Rectangle((215,300),(231,350))
backFoot2.draw(win)
backFoot2.fill = makeColor("brown")

frontFoot1 = Rectangle((270,300),(283,350))
frontFoot1.draw(win)
frontFoot1.fill = makeColor("brown")

dog = Oval((250,300),46,20)
dog.draw(win)
dog.fill = makeColor("brown")

backFoot1 = Rectangle((204,300),(220,350))
backFoot1.draw(win)
backFoot1.fill = makeColor("brown")

frontFoot2 = Rectangle((280,300),(293,350))
frontFoot2.draw(win)
frontFoot2.fill = makeColor("brown")

head = Circle((292,282),25)
head.draw(win)
head.fill = makeColor("brown")

eye1 = Circle((280,280),7)
eye1.draw(win)
eye1.fill = makeColor("white")

pupil1 = Circle((280,280),2)
pupil1.draw(win)
pupil1.fill = makeColor("black")

eye2 = Circle ((305,280),7)
eye2.draw(win)
eye2.fill = makeColor("white")

pupil2 = Circle((305,280),2)
pupil2.draw(win)
pupil2.fill = makeColor("black")

smile = Curve((280,290),(290,305),(300,305),(310,290))
smile.draw(win)

tail = Curve((210,290),(200,305),(190,290),(180,295))
tail.draw(win)

trunk1 = Rectangle((50,170),(80,300))
trunk1.draw(win)
trunk1.fill = makeColor("brown")

leaves1 = Circle((40,160),30)
leaves1.draw(win)
leaves1.fill = makeColor("green")

leaves2 = Circle((70,145),30)
leaves2.draw(win)
leaves2.fill = makeColor("green")

leaves3 = Circle((95,175),30)
leaves3.draw(win)
leaves3.fill = makeColor("green")

sun = Circle((450,50),50)
sun.draw(win)
sun.fill = makeColor("yellow")

text = Text((250,430),"This is Fred, Fred says 'Hi'")
text.draw(win)
text.fill = Color("orange")
text.fontSize = 30

bubble = Oval((400,290),80,35)
bubble.draw(win)
bubble.fill = makeColor("white")

hi = Text((400,290), "What's up, Chase?")
hi.draw(win)
hi.fill = COlor("black")
hi.fontsize = 3


