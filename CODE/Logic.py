import sys

from tabulate import tabulate

import Admin
import Students
import Teacher

while True:
    table = [{1, "Admin"}, [2, "Teacher"], [3, 'Student'], ['*', 'Exit']]
    headers = ['Id', "Options"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))# tabulate is used for printing the menu
    desig: str or int = input('Enter Your Option: ').upper()
    if desig == '1' or desig == 'ADMIN':
        Admin.admin()
    elif desig == '2' or desig == 'TEACHER':
        Teacher.teacher()
    elif desig == '3' or desig == 'STUDENT':
        Students.student()
    elif desig == '*' or desig == 'EXIT':
        print("Thank You")
        sys.exit()
    else:
        print('Enter A Valid Option')