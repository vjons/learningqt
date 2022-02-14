import sys
#Importing QtWidgets by using the alias QW for conveniance
import PyQt5.QtWidgets as QW

#In order to have a menubar and statubar we can sub class QMainWindow
class CustomWindow(QW.QMainWindow):
	'''Documentation of this class is written enclosed like this:
	\'\'\'<text>\'\'\' in the beginning of the class and can be reached
	from the __doc__ property.'''
	def __init__(self):
		super().__init__()
		self.setWindowTitle("CustomQMainWindow")
		self.setMinimumSize(600,400)
				
		#Creating a fileMenu
		fileMenu=self.menuBar().addMenu("File")
		
		#Creating an action that should trigger the close function which already exists in QMainWindow
		action=QW.QAction("Take me out of here!",self,triggered=self.close)
		fileMenu.addAction(action)
		
		helpMenu=self.menuBar().addMenu("Help me")
		
		#Creating an action that should trigger the showMessage function
		action=QW.QAction("What is this program?",self,triggered=self.showMessage)
		helpMenu.addAction(action)
		
		#Getting the statusbar instance and setting the message to be displayed.
		self.statusBar().showMessage("Status Bar: This message will be removed when the menus are used")
		
	def showMessage(self):
		#Helpfull class to show short messages on the screen
		QW.QMessageBox.about(self, "About",self.__doc__)

if __name__ == '__main__':
	app=QW.QApplication.instance()
	if not app:
		app=QW.QApplication([])
	window=CustomWindow()#Instantiating your custom window
	window.show()
	sys.exit(app.exec_())