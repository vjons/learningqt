#Importing the sys module (used for talking to other programs and accessing the file system on the computer)
import sys

#Importing the class QWidget and QApplication from the PyQt5.QtWidgets module
from PyQt5.QtWidgets import QWidget,QApplication

#Does not run if this file only is imported
if __name__ == '__main__':
	#getting the current application instance (useful if running with interactively)
	app=QApplication.instance()

	#If no application instance was found we create a new application instance
	if not app:
		app=QApplication([])

	#Creating a default window and showing it
	widget=QWidget()
	widget.show()

	#When application finishes, exit program
	sys.exit(app.exec_())