import time
from graphics import *

win = GraphWin('MyWin', 1000, 600)

sky = Rectangle(Point(0, 0), Point(1000, 350))
sky.setFill("#8cfffb")
sky.setOutline("#8cfffb")

ground = Rectangle(Point(0, 350), Point(1000, 600))
ground.setFill("#585858")
ground.setOutline("#585858")

def Magic_Humans(face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y):
	kx = ((X - 300) / 550)
	ky = ((Y - 500) / 550)
	for i in range(550):
		time.sleep(0.002)
		face_an.move(-1*kx, -1*ky)
		body_an.move(-1*kx, -1*ky)
		leg1_an.move(-1*kx, -1*ky)
		leg2_an.move(-1*kx, -1*ky)
		arm1_an.move(-1*kx, -1*ky)
		arm2_an.move(-1*kx, -1*ky)
	for i in range (37):
		time.sleep(0.002)
		face_an.move(0, -1)
		body_an.move(0, -1)
		leg1_an.move(0, -1)
		leg2_an.move(0, -1)
		arm1_an.move(0, -1)
		arm2_an.move(0, -1)
	face_an.undraw()
	body_an.undraw()
	leg1_an.undraw()
	leg2_an.undraw()
	arm1_an.undraw()
	arm2_an.undraw()

def Cloud(X, Y, K, color, N):
	for i in range (N):
		cloud = Circle(Point(X+40*i, Y), 50*K)
		cloud.setFill(color)
		cloud.setOutline(color)
		cloud.draw(win)

def Stupid_Human(X, Y, K, color, armsTF):
	face = Circle(Point(X, Y), 15*K)
	face.setFill(color)
	face.setOutline(color)
	body = Line(Point(X, Y+15*K), Point(X, Y+55*K))
	body.setOutline(color)
	leg1 = Line(Point(X, Y+55*K), Point(X+15*K, Y+85*K))
	leg1.setOutline(color)
	leg2 = Line(Point(X, Y+55*K), Point(X-15*K, Y+85*K))
	leg2.setOutline(color)
	arm1 = Line(Point(X, Y+15*K), Point(X+15*K, Y+55*K))
	arm1.setOutline(color)
	arm2 = Line(Point(X, Y+15*K), Point(X-15*K, Y+55*K))
	arm2.setOutline(color)
	face.draw(win)
	body.draw(win)
	leg1.draw(win)
	leg2.draw(win)
	if armsTF==True:
		arm1.draw(win)
		arm2.draw(win)
	return face, body, leg1, leg2, arm1, arm2, X, Y


def Sun(X, Y, R, colorIn, colorOut):
	sun = Circle(Point(X, Y), R)
	sun.setFill(colorIn)
	sun.setOutline(colorOut)
	sun.setWidth(5)
	sun.draw(win)

def Tree(X, Y, R, crownIn, crownOut, stemIn, stemOut, appleTF):
	tree_crown = Circle(Point(X, Y), R)
	tree_crown.setFill(crownIn)
	tree_crown.setOutline(crownOut)
	tree_crown.setWidth(5)
	tree_stem = Polygon(Point(X-7, Y+120), Point(X, Y), Point(X+7, Y+120), Point(X-7, Y+120))
	tree_stem.setFill(stemIn)
	tree_stem.setOutline(stemOut)
	tree_stem.setWidth(2)
	tree_stem.draw(win)
	tree_crown.draw(win)
	apple = Circle(Point(X+15, Y-5), 5)
	apple.setFill("red")
	apple.setOutline("red")
	if appleTF==True:
		apple.draw(win)



def House(X, Y, K, roofC, houseC, flagsTF):
	house = Rectangle(Point(X, Y), Point(X+340*K, Y+330*K))
	house.setFill(houseC)
	house.setOutline(houseC)
	house.setWidth(2*K)

	roof = Polygon(Point(X-40*K, Y), Point(X+170*K, Y-170*K), Point(X+380*K, Y), Point(X-40*K, Y))
	roof.setFill(roofC)
	roof.setOutline(roofC)


	def Walls(a):
		wall = Line(Point(X, Y+a), Point(X+340*K, Y+a))
		wall.setOutline("#b97a56")
		wall.setWidth(2*K)
		wall.draw(win)

	door = Rectangle(Point(X+140*K, Y+210*K), Point(X+200*K, Y+330*K))
	door.setFill("#b97a56")
	door.setOutline("#000000")
	door.setWidth(4*K)

	doorhand = Circle(Point(X+150*K, Y+270*K), 5*K)
	doorhand.setFill("#ffca18")
	doorhand.setOutline("#000000")
	doorhand.setWidth(2*K)

	doorstep = Rectangle(Point(X+110*K, Y+330*K), Point(X+230*K, Y+350*K))
	doorstep.setFill("#b97a56")
	doorstep.setOutline("#000000")
	doorstep.setWidth(4*K)

	window0 = Circle(Point(X+170*K, Y-70*K), 35*K)
	window0.setFill("#00a8f3")
	window0.setOutline("#000000")
	window0.setWidth(4*K)

	wline01 = Line(Point(X+170*K, Y-105*K), Point(X+170*K, Y-35*K))
	wline01.setWidth(4*K)

	wline02 = Line(Point(X+135*K, Y-70*K), Point(X+205*K, Y-70*K))
	wline02.setWidth(4*K)

	window1 = Rectangle(Point(X+20*K, Y+210*K), Point(X+120*K, Y+290*K))
	window1.setFill("#00a8f3")
	window1.setOutline("#000000")
	window1.setWidth(4*K)

	wline11 = Line(Point(X+20*K, Y+240*K), Point(X+120*K, Y+240*K))
	wline11.setWidth(4*K)

	wline12 = Line(Point(X+70*K, Y+210*K), Point(X+70*K, Y+290*K))
	wline12.setWidth(4*K)

	window2 = Rectangle(Point(X+220*K, Y+210*K), Point(X+320*K, Y+290*K))
	window2.setFill("#00a8f3")
	window2.setOutline("#000000")
	window2.setWidth(4*K)

	wline21 = Line(Point(X+220*K, Y+240*K), Point(X+320*K, Y+240*K))
	wline21.setWidth(4*K)

	wline22 = Line(Point(X+270*K, Y+210*K), Point(X+270*K, Y+290*K))
	wline22.setWidth(4*K)

	wbalcony = Rectangle(Point(X+70*K, Y+40*K), Point(X+270*K, Y+140*K))
	wbalcony.setFill("#00a8f3")
	wbalcony.setOutline("#000000")
	wbalcony.setWidth(4*K)

	bwline1 = Line(Point(X+120*K, Y+40*K), Point(X+120*K, Y+110*K))
	bwline1.setWidth(4*K)

	bwline2 = Line(Point(X+220*K, Y+40*K), Point(X+220*K, Y+110*K))
	bwline2.setWidth(4*K)

	balcony = Rectangle(Point(X+50*K, Y+110*K), Point(X+290*K, Y+160*K))
	balcony.setFill("#b97a56")
	balcony.setOutline("#000000")
	balcony.setWidth(2*K)

	bline1 = Line(Point(X+50*K, Y+110*K), Point(X+170*K, Y+160*K))
	bline1.setWidth(2*K)

	bline2 = Line(Point(X+170*K, Y+160*K), Point(X+290*K, Y+110*K))
	bline2.setWidth(2*K)


	def Flags(F, color):
		flag = Polygon(Point(F, Y), Point(F+21*K, Y+30*K), Point(F+42*K, Y), Point(F, Y))
		flag.setFill(color)
		flag.setOutline("#000000")
		flag.setWidth(2*K)
		flag.draw(win)



			#START_MAIN_CODE

	house.draw(win)				#START_House
	roof.draw(win)
	width = 20*K
	for i in range(9):
		Walls(width)
		width += 20*K

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

	if flagsTF==True:
		R1 = X-40*K					#START_Flags
		for j in range(2):
			Flags(R1, "#b83dba")
			R1 += 210*K
		R2 = X+2*K
		for j in range(2):
			Flags(R2, "#fff200")
			R2 += 210*K
		R3 = X+44*K
		for j in range(2):
			Flags(R3, "#ec1c24")
			R3 += 210*K
		R4 = X+86*K
		for j in range(2):
			Flags(R4, "#0ed145")
			R4 += 210*K
		R5 = X+128*K
		for j in range(2):
			Flags(R5, "#3f48cc")
			R5 += 210*K
#END DEFHOUSE

sky.draw(win)
ground.draw(win)


Sun(75, 75, 50, "#fff200", "#ffca18")
Sun(575, 75, 30, "red", "#ffca18")
Cloud(700, 100, 1, "white", 3)
Tree(600, 450, 50, "#0ed145", "#73eb26", "#b97a56", "#585858", appleTF=True)
Tree(70, 450, 50, "#0ed145", "#73eb26", "#b97a56", "#585858", appleTF=False)
House(130, 220, 1, "#88001b", "#fdeca6", flagsTF=True)
House(660, 320, 0.5, "blue", "yellow", flagsTF=False)
House(880, 400, 0.3, "white", "red", flagsTF=True)

face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y = Stupid_Human(850, 500, 1, "green", armsTF=True)
Magic_Humans(face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y)
face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y = Stupid_Human(785, 528, 1.6, "red", armsTF=True)
Magic_Humans(face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y)
face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y = Stupid_Human(472, 365, 0.9, "black", armsTF=False)
Magic_Humans(face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y)
face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y = Stupid_Human(541, 156, 1.3, "yellow", armsTF=True)
Magic_Humans(face_an, body_an, leg1_an, leg2_an, arm1_an, arm2_an, X, Y)



#WHO DID DO THIS F***ING CODE?!


win.getMouse()
win.close()