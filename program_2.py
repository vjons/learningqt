import sys

#Import all modules from PyQt5.QtWidgets (this should not be done like this,
#look in the next tutorial for the best way to do it)
from PyQt5.QtWidgets import *


#Definition of window sizes
left=100
top=100
width=400
height=400

minWidth=200
minHeight=200

maxWidth=800
maxHeight=800

#Define you own custom widget that inherits all properties from QWidget
#You can then include your own custom features
class CustomWidget(QWidget):
	
	#All functions in a class has "self" as the first parameter
	def __init__(self):
		#Initialize the super class, that is the QWidget class
		super().__init__()
		#Setting the text shown in the top left of the window
		self.setWindowTitle("CustomWidget")
		
		#Setting starting geometry of window
		self.setGeometry(left,top,width,height)
		
		#Setting the minimum dimensions of your window
		self.setMinimumSize(minWidth,minHeight) 
		
		#Setting the maximum height and width of your window
		#Notice that when this is set the window can not be maximized
		self.setMaximumSize(maxWidth,maxHeight)

if __name__ == '__main__':
	app=QApplication.instance()
	if not app:
		app=QApplication([])
	widget=CustomWidget()#Instantiating your custom widget
	widget.show()
	sys.exit(app.exec_())