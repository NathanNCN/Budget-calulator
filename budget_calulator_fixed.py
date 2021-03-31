from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.QtGui import *
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.weekly_expenses = 0
        self.famliy_income = {}

    def initUI(self):
        self.setGeometry(200, 200, 700, 500)
        self.setWindowTitle("Budget")


        # user_inputs: Button to add family member with their name and their weekly income
        # button
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Added")
        self.label.move(10, 320)
        self.label.hide()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Add person!")
        self.b1.clicked.connect(self.add_person)
        self.b1.move(70, 450)

        # input box for name of person
        self.textbox = QLineEdit(self)
        self.textbox.setText("name")
        self.textbox.move(21, 340)
        self.textbox.resize(200, 40)

        # input box for person income
        self.textbox2 = QLineEdit(self)
        self.textbox2.setText("weekly income")
        self.textbox2.move(21, 400)
        self.textbox2.resize(90, 40)

        # input box for % of their income they want to spend on the weekly epxnses
        self.textbox3 = QLineEdit(self)
        self.textbox3.setText("Percentage")
        self.textbox3.move(130, 400)
        self.textbox3.resize(90, 40)

        # input box for weekly expsense
        self.textbox_expesnives = QLineEdit(self)
        self.textbox_expesnives.setText("food cost")
        self.textbox_expesnives.move(250, 400)
        self.textbox_expesnives.resize(100, 40)

        self.textbox_expesnives2 = QLineEdit(self)
        self.textbox_expesnives2.setText("transportation cost")
        self.textbox_expesnives2.move(250, 340)
        self.textbox_expesnives2.resize(100, 40)

        self.textbox_expesnives3 = QLineEdit(self)
        self.textbox_expesnives3.setText("entertainment cost")
        self.textbox_expesnives3.move(360, 340)
        self.textbox_expesnives3.resize(100, 40)

        self.textbox_expesnives4 = QLineEdit(self)
        self.textbox_expesnives4.setText("random cost")
        self.textbox_expesnives4.move(360, 400)
        self.textbox_expesnives4.resize(100, 40)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(305, 450)
        self.b2.setText("weekly expenses")
        self.b2.clicked.connect(self.weekly_expnses_saved)
        self.b2.setEnabled(False)

        # calculate if they are in buget button
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Calculate")
        self.b3.move(500, 350)
        self.b3.resize(150, 80)
        self.b3.clicked.connect(self.calulate_budget)
        self.b3.setEnabled(False)

        self.label3 = QtWidgets.QLabel('Arial font', self)
        self.label3.setFont(QFont('Times', 15))
        self.label3.setText("")
        self.label3.move(50, 150)
        self.label3.hide()
    def if_varible_isnumeric(self,values):
        for value in values:
            if value.isdigit()==False:
                sys.exit()

    def add_person(self):
        name_of_person = self.textbox.text()
        amount_of_income = self.textbox2.text()
        percentage_of_income = self.textbox3.text()
        if amount_of_income.isdigit() == False or percentage_of_income.isdigit() == False or float(
                percentage_of_income) > 100:
            sys.exit()
        amount_of_income_contribution = float(percentage_of_income) * float(amount_of_income) / 100
        self.famliy_income.update({name_of_person: amount_of_income_contribution})
        self.label.setText(
            f"{name_of_person} and is contrubuting {amount_of_income_contribution}.That is {percentage_of_income} of their weekly income.")
        self.label.setFont(QFont('Times', 10))
        self.label.adjustSize()
        self.label.show()
        self.b2.setEnabled(True)

    def weekly_expnses_saved(self):
        expense_food = self.textbox_expesnives.text()
        expense_transportion = self.textbox_expesnives2.text()
        expense_entertainment = self.textbox_expesnives3.text()
        expense_other = self.textbox_expesnives4.text()
        values=[expense_other,expense_food,expense_entertainment,expense_transportion]
        self.if_varible_isnumeric(values)

        self.weekly_expenses += float(expense_food) + float(expense_transportion) + float(expense_entertainment) + float(expense_other)
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText(f"{self.weekly_expenses}")
        self.label2.move(360, 320)
        self.label2.show()
        self.b2.setEnabled(False)
        self.b3.setEnabled(True)

    def calulate_budget(self):
        whole_budget = sum(self.famliy_income.values())
        biggest_contributor = max(self.famliy_income.values())
        if whole_budget >= self.weekly_expenses:
            self.label3.setText(f"You are under budget with {abs(whole_budget-self.weekly_expenses)} $ left over. Great job budgeting.\n\n The biggest contributor payed {biggest_contributor}$")
            self.label3.adjustSize()
            self.label3.show()
        else:
            self.label3.setText(f"You are over {abs(whole_budget-self.weekly_expenses)} $ over the budget. Do better.\n\nThe biggest contributor payed {biggest_contributor}$")
            self.label3.adjustSize()
            self.label3.show()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


main()
