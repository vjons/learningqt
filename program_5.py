import sys
import PyQt5.QtWidgets as QW


#Creating the login dialog, a QDialog can't be maximized nor minimized
class Login(QW.QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login")
		self.setFixedSize(360,100)
		
		#Storing users
		self.users={"viktor":"beachvolley","christoffer":"sundstrom"}
		
		#Creating a layout that we can use to align things inside a widget
		#For this layout we can specify (row,column,row span,column span) for each object that we add to it
		layout=QW.QGridLayout(self)
		
		#Creating to labels that display text
		label1=QW.QLabel("Username:")
		label2=QW.QLabel("Password:")
		
		
		#Creating Fields that can be written
		#Using self here means that the data is available from other methods in the class even when this method is done.
		self.usernameEdit=QW.QLineEdit()
		self.passwordEdit=QW.QLineEdit()
		self.passwordEdit.setEchoMode(QW.QLineEdit.Password)
		
		
		#Creating 2 buttons and setting the text on them
		button1=QW.QPushButton("Login")
		button2=QW.QPushButton("Register")
		
		#Telling the program what functions to run when the user presses the buttons
		button1.pressed.connect(self.checkPassword)
		button2.pressed.connect(self.createNewUser)
		
		#Adding all the components to the layout
		layout.addWidget(label1,0,0,1,1)
		layout.addWidget(label2,0,2,1,1)
		layout.addWidget(self.usernameEdit,0,1,1,1)
		layout.addWidget(self.passwordEdit,0,3,1,1)
		layout.addWidget(button1,1,0,1,2)
		layout.addWidget(button2,1,2,1,2)
	
	#Checking if a username and password matches available credentials
	def checkPassword(self):
		username=self.usernameEdit.text()
		if username in self.users:
			password=self.passwordEdit.text()
			if password==self.users[username]:
				#This call sets the Accepted property to True
				self.accept()
			else:
				QW.QMessageBox.about(self,"Login failed","Username exists but password does not match")
		else:
			QW.QMessageBox.about(self,"Login failed","Username does not exist")
		
	#Creating a new user from the username and password written in the fields
	def createNewUser(self):
		username=self.usernameEdit.text()
		password=self.passwordEdit.text()
		
		if username and password:
			self.users[username]=password
			QW.QMessageBox.about(self,"New user","You are now registered!")
		else:
			QW.QMessageBox.about(self,"Creation Failed","No {} given!".format("username" if password else "password"))

#Simple window that you will get to if login was successful
class UserWindow(QW.QMainWindow):
	def __init__(self):
		QW.QWidget.__init__(self)
		self.setMinimumSize(600,400)

		fileMenu=self.menuBar().addMenu("File")
		action=QW.QAction("Quit",self,triggered=self.close)
		fileMenu.addAction(action)

if __name__ == '__main__':
	app=QW.QApplication.instance()
	if not app:
		app=QW.QApplication([])
	login = Login()
	#Check if the credentials given were accepted, if so create the window.
	if login.exec_() == QW.QDialog.Accepted:
		window = UserWindow()
		window.setWindowTitle(login.usernameEdit.text())
		window.show()
		sys.exit(app.exec_())