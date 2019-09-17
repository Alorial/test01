from graphics import *

win = GraphWin('MyWin', 600, 600)

sky = Rectangle(Point(0, 0), Point(600, 480))	
sky.setFill("#8cfffb")
sky.setOutline("#8cfffb")

ground = Rectangle(Point(0, 480), Point(600, 600))
ground.setFill("#585858")
ground.setOutline("#585858")

sun = Circle(Point(75, 75), 50)
sun.setFill("#fff200")
sun.setOutline("#ffca18")
sun.setWidth(5)

def Tree(P):
	tree_crown = Circle(Point(P, 450), 50)
	tree_crown.setFill("#0ed145")
	tree_crown.setOutline("#73eb26")
	tree_crown.setWidth(5)
	tree_stem = Polygon(Point(P - 7, 570), Point(P, 450), Point(P + 7, 570), Point(P - 7, 570))
	tree_stem.setFill("#b97a56")
	tree_stem.setOutline("#585858")
	tree_stem.setWidth(2)
	tree_crown.draw(win)
	tree_stem.draw(win)

house = Rectangle(Point(130, 220), Point(470, 550))
house.setFill("#fdeca6")
house.setOutline("#b97a56")
house.setWidth(2)

roof = Polygon(Point(90, 220), Point(300, 50), Point(510, 220), Point(90, 220))
roof.setFill("#88001b")
roof.setOutline("#88001b")

def Walls(a):
	wall = Line(Point(130, 220 + a), Point(470, 220 + a))
	wall.setOutline("#b97a56")
	wall.setWidth(2)
	wall.draw(win)

door = Rectangle(Point(270, 430), Point(330, 550))
door.setFill("#b97a56")
door.setOutline("#000000")
door.setWidth(4)

doorhand = Circle(Point(280, 490), 5)
doorhand.setFill("#ffca18")
doorhand.setOutline("#000000")
doorhand.setWidth(2)

doorstep = Rectangle(Point(240, 550), Point(360, 570))
doorstep.setFill("#b97a56")
doorstep.setOutline("#000000")
doorstep.setWidth(4)

window0 = Circle(Point(300, 150), 35)
window0.setFill("#00a8f3")
window0.setOutline("#000000")
window0.setWidth(4)

wline01 = Line(Point(300, 115), Point(300, 185))
wline01.setWidth(4)

wline02 = Line(Point(265, 150), Point(335, 150))
wline02.setWidth(4)

window1 = Rectangle(Point(150, 430), Point(250, 510))
window1.setFill("#00a8f3")
window1.setOutline("#000000")
window1.setWidth(4)

wline11 = Line(Point(150, 460), Point(250, 460))
wline11.setWidth(4)

wline12 = Line(Point(200, 430), Point(200, 510))
wline12.setWidth(4)

window2 = Rectangle(Point(350, 430), Point(450, 510))
window2.setFill("#00a8f3")
window2.setOutline("#000000")
window2.setWidth(4)

wline21 = Line(Point(350, 460), Point(450, 460))
wline21.setWidth(4)

wline22 = Line(Point(400, 430), Point(400, 510))
wline22.setWidth(4)

wbalcony = Rectangle(Point(200, 260), Point(400, 360))
wbalcony.setFill("#00a8f3")
wbalcony.setOutline("#000000")
wbalcony.setWidth(4)

bwline1 = Line(Point(250, 260), Point(250, 330))
bwline1.setWidth(4)

bwline2 = Line(Point(350, 260), Point(350, 330))
bwline2.setWidth(4)

balcony = Rectangle(Point(180, 330), Point(420, 380))
balcony.setFill("#b97a56")
balcony.setOutline("#000000")
balcony.setWidth(2)

bline1 = Line(Point(180, 330), Point(300, 380))
bline1.setWidth(2)

bline2 = Line(Point(300, 380), Point(420, 330))
bline2.setWidth(2)

def Flags (F, color):
	flag = Polygon(Point(F, 220), Point(F + 21, 250), Point(F + 42, 220), Point(F, 220))
	flag.setFill(color)
	flag.setOutline("#000000")
	flag.setWidth(2)
	flag.draw(win)



		#START_MAIN_CODE
sky.draw(win)
ground.draw(win)
sun.draw(win)
Tree(65)
Tree(535)

house.draw(win)				#START_House
roof.draw(win)
width = 20	
for i in range (9):
	Walls(width)
	width += 20

door.draw(win)				#START_Door
doorhand.draw(win)	
doorstep.draw(win)

window0.draw(win)			#START_Windows
wline01.draw(win)
wline02.draw(win)

window1.draw(win)
wline11.draw(win)
wline12.draw(win)

window2.draw(win)
wline21.draw(win)
wline22.draw(win)

wbalcony.draw(win)			#START_Balcony
bwline1.draw(win)
bwline2.draw(win)
balcony.draw(win)
bline1.draw(win)
bline2.draw(win)

R1 = 90					#START_Flags
for j in range (2):
	Flags (R1, "#b83dba")
	R1 += 210
R2 = 132
for j in range (2):
	Flags (R2, "#fff200")
	R2 += 210
R3 = 174
for j in range (2):
	Flags (R3, "#ec1c24")
	R3 += 210
R4 = 216
for j in range (2):
	Flags (R4, "#0ed145")
	R4 += 210
R5 = 258
for j in range (2):
	Flags (R5, "#3f48cc")
	R5 += 210



win.getMouse()
win.close()