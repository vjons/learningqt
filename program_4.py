import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC

class MyWidget(QW.QWidget):

	#Defining the signal and what type of data that is sent when the signals is emitted
	mouseMove=QC.pyqtSignal(int,int)
	def __init__(self):
		super().__init__()

		#Mouse tracking needs to be turned on
		self.setMouseTracking(True)	

	#Tracking mouse positions where the event parameter holds information about the mouse 
	def mouseMoveEvent(self,event):
		#Mouse is moving, so we emit mouseMove signal and includes the position in pixels from top left
		self.mouseMove.emit(event.x(),event.y())
		
	#Register mouse button clicks
	def mousePressEvent(self,event):
		#When right mouse button is clicked, you can open a context menu
		if event.button()==2:			
			menu = QG.QMenu(self)
			#Create an action that can be added to the context menu
			action=QW.QAction("do something",self,triggered=self.someFunction)
			menu.addAction(action)
			#show the menu at the cursor position
			menu.popup(QG.QCursor().pos())
			
			
	#The function that is executed when the action "do something" is triggered
	def someFunction(self):
	    print("did something")
		
		
class CustomWindow(QW.QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Window that shows mousePosition")
		self.setMinimumSize(600,400)

		fileMenu=self.menuBar().addMenu("File")
		action=QW.QAction("Quit",self,triggered=self.close)
		fileMenu.addAction(action)
		
		#creating a customWidget and setting it as the centralWidget in my CustomWindow
		widget = MyWidget()
		self.setCentralWidget(widget)
		
		#Connecting a an action or signal to a function that triggers when mouseMove signal in widget is emitted
		widget.mouseMove.connect(self.showMousePosition)
		
	def showMousePosition(self,x,y):
		#Showing a message in the status bar. the format function of strings replaces {} with the argument in the order they appear
		self.statusBar().showMessage("Mouse position: ({}, {})".format(x,y))


if __name__ == '__main__':		
	app=QW.QApplication.instance()
	if not app:
		app=QW.QApplication([])
	window=CustomWindow()
	window.show()
	sys.exit(app.exec_())