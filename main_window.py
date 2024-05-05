import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QStatusBar, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QAction, QGuiApplication as qApp

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the main window's properties
        self.setWindowTitle('Financial Planner')
        self.setGeometry(300,300,600,400) #Position x,y, width, height

        #Create a status bar
        self.statusBar().showMessage('Ready')

        #Create a menu bar with one 'File' Menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        # Add exit action to the 'File' menu
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)

        # Initialize the UI components
        self.initUI()
    
    def initUI(self):
        #Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Layout
        layout = QVBoxLayout()

        #Income Field
        self.income_label = QLabel('Montly Income:')
        self.income_edit = QLineEdit()
        layout.addWidget(self.income_label)
        layout.addWidget(self.income_edit)

        #Expenses Field
        self.expense_label = QLabel('Monthly Expenses:')
        self.expense_edit = QLineEdit()
        layout.addWidget(self.expense_label)
        layout.addWidget(self.expense_edit)

        #Balance Field
        self.balance_label = QLabel('Current Balance:')
        self.balance_edit = QLineEdit()
        layout.addWidget(self.balance_label)
        layout.addWidget(self.balance_edit)

        # Submit Button
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.process_financial_data)
        layout.addWidget(self.submit_button)

        # Set layout
        central_widget.setLayout(layout)

    def process_financial_data(self):
        income = self.income_edit.text()
        expense = self.expense_edit.text()
        balance = self.balance_edit.text()
        print(f"Income: {income}, Expenses: {expense}, Balance: {balance}")

    def run(self):
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.run()
    sys.exit(app.exec())