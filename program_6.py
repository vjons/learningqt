import sys
import os
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

#Getting the directory of this file
FILE_DIR = os.path.dirname(os.path.realpath(__file__))

#Is used by addMenuBar (it is a little bit hard to understand exactly what it does. But basically it is a function that returns a function
def create_func(title):
	def f(self=None):
		print(title)
	return f

#Function I wrote to add menus and actions to the menubar that you specify in the file "filename"
#I alittle bit hard to understand, but it is easy to use see the example file "menubar.txt"
def addMenuBar(self,filename):
	with open(filename,'r') as file:
		data=[[next((i for i,c in enumerate(line) if not c=="\t"),0)]+\
		line.strip("\n\t").split(":")+[""]*(2-line.count(":")) for line in file]
		menus=[self.menuBar()]
		for depth,title,name,short in data:
			if name and not hasattr(self,name):
				setattr(self,name,create_func(title))
			menus=menus[:depth+1]
			if all(t=="-" for t in title):
				menus[-1].addSeparator()
			elif name:
				menus[-1].addAction(title,getattr(self,name),shortcut=QG.QKeySequence(short))
			else:
				menus.append(menus[-1].addMenu(title))

#Widget with multi touch functionality
class MultiTouchWidget(QW.QWidget):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(600,400)

		#Storing a list of colors
		self.colors=["black","green","blue","cyan","red","yellow","magenta"]
		
		#Dictionary of points (first value in point lists are the touch id)
		self.points={}
	
	#This function is doing all the painting
	def paintEvent(self, event):
		#Create a painter object
		paint = QG.QPainter()
		
		#Being paint session 
		paint.begin(self)
		
		#Paint the backgroun white
		paint.fillRect(self.rect(),QG.QBrush(QG.QColor("white")))
		
		#Looping through all values in self.points and draws each touch path
		for points in self.points.values():
			id0,points=points[0],points[1:]
			#Sets the border/pen color
			id=id0%len(self.colors)
			paint.setPen(QG.QColor(self.colors[id%len(self.colors)]))
			
			#Setting the filling color QBrush() gives no fill
			paint.setBrush(QG.QBrush(QG.QColor(self.colors[id])))
		
			#Drawing a circle centered at the first point
			paint.drawEllipse(points[0][0]-2,points[0][1]-2,4,4)
			
			#Draw lines if there is more then 1 point in points
			if len(points)>1:
				#Creating the lines from neighbouring points
				lines=[QC.QLine(*p0,*p1) for p0,p1 in zip(points[:-1],points[1:])]
				paint.drawLines(*lines)
		
		#End the paint session
		paint.end()
	
	#Method to add point to point list
	def addPoint(self,id,p0,p):
		self.points.setdefault((p0.x(),p0.y()),[id])
		self.points[(p0.x(),p0.y())].append((p.x(),p.y()))
	
	#Reading touch event
	def event(self,event):
		if event.type() in (QC.QEvent.TouchBegin,QC.QEvent.TouchUpdate,QC.QEvent.TouchEnd):
			for tp in event.touchPoints():
				self.addPoint(tp.id(),tp.startPos(),tp.pos())
			self.repaint()
		return QW.QWidget.event(self,event)

	#If only one touch point it is seen as a mousePress and move
	def mousePressEvent(self,event):
		self.mdpos=event.pos()
		self.addPoint(0,self.mdpos,self.mdpos)
		self.repaint()
		
		#setting that the mouse/finger is pressed on the screen
		self.md=True
		
	
	def mouseReleaseEvent(self,event):
		#When releasing the button/finger it is set to false
		self.md=False
		
	def mouseMoveEvent(self,event):
		#Add points to points-list only if mousebutton/finger is pressed on the screen
		if self.md:
			self.addPoint(0,self.mdpos,event.pos())
			self.repaint()
			

class MainWindow(QW.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Multitouch Window")
		self.widget=MultiTouchWidget()
		self.setCentralWidget(self.widget)
		addMenuBar(self,os.path.join(FILE_DIR,"menubar_6.txt"))
		
	#Clearing the screen by setting the points-list to empty and repainting the widget.
	def clear(self):
		self.widget.points={}
		self.widget.repaint()
	
		
if __name__ == '__main__':		
	app=QW.QApplication.instance()
	if not app:
		app=QW.QApplication([])
	main=MainWindow()
	main.show()
	sys.exit(app.exec_())