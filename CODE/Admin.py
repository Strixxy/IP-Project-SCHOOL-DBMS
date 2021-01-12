import datetime
import sys

import mysql.connector as sql
from prettytable import PrettyTable
from tabulate import tabulate

conn = sql.connect(host='localhost', user='root', password='1234', database='project')
mycursor = conn.cursor()


def admin():
    while True:
        adm_table = [[1, "Student Registration"], [2, "Employee Registration"], [3, 'Student Details'],
                     [4, 'Employee Details'], [0, 'Go Back To Main Menu'], ['*', 'EXIT']]
        adm_headers = ['Admin Menu']
        print(tabulate(adm_table, adm_headers, tablefmt="fancy_grid", floatfmt=".1f"))
        choice: str or int = input('Enter Your Choice: ').upper()
        if choice == '1' or choice == 'Student Registration':
            stdregister()
        elif choice == '2' or choice == 'Employee Registration':
            empregister()
        elif choice == '3' or choice == 'Student Details':
            stdlist()
        elif choice == '4' or choice == ' Employee Details':
            emplist()
        elif choice == '0' or choice == ' Go Back To Main Menu':
            break
        elif choice == '*' or choice == 'EXIT':
            print('Thank You')
            sys.exit()
        else:
            print('Enter An Valid Option')


def stdregister():
    std_headers = ['Selected Option']
    std_table = [['Student Register']]
    print(tabulate(std_table, std_headers, tablefmt="fancy_grid", floatfmt=".1f"))
    STD_NAME = input("Enter the Name: ")
    STD_GRADEE = int(input("Enter the grade: "))
    STD_NO = int(input("Enter Your Phone Number: "))
    year = int(input("Enter The Year: "))
    month = int(input('Enter The Month: '))
    day = int(input('Enter The Day: '))
    STD_AGE = datetime.datetime(year, month, day)
    STD_ADDRESS = input('Enter The Address: ')

    mycursor.execute(
        "insert into students(STD_NAME, STD_GRADEE, STD_AGE,STD_NUMBER, STD_ADDRESS)"
        "values('{}', '{}', '{}', '{}', '{}')"
        .format(STD_NAME, STD_GRADEE, STD_AGE,STD_NO, STD_ADDRESS))
    conn.commit()
    print('***********Entry Successful***********')


def empregister():
    teach_headers = ['Selected Option']
    teach_table = [['Teacher Register']]
    print(tabulate(teach_table, teach_headers, tablefmt="fancy_grid", floatfmt=".1f"))
    TEACHER_NAME = input("Enter the Name: ")
    TEACHER_DEPT = input("Enter the department: ")
    TEACHER_NO = int(input('Enter Your Contact Number: '))
    year = int(input("Enter The Year: "))
    month = int(input('Enter The Month: '))
    day = int(input('Enter The Day: '))
    TEACHER_AGE = datetime.datetime(year, month, day)
    mycursor.execute(
        "insert into teacher ( TEACHER_NAME, TEACHER_DEPT, TEACHER_NO, TEACHER_AGE) "
        "values('{}', '{}', '{}','{}')".format(TEACHER_NAME, TEACHER_DEPT, TEACHER_NO, TEACHER_AGE))
    conn.commit()
    print('***********Entry Successful***********')


def stdlist():
    headers = ['Selected Option']
    table = [['Student Details']]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    mycursor.execute("select * from students")
    results = mycursor.fetchall()
    t = PrettyTable(['STD_ID', 'STD_NAME', 'STD_GRADE', 'STD_AGE', 'STD_NUMBER', 'STD_ADDRESS'])
    for STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER, STD_ADDRESS in results:
        t.add_row([STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER, STD_ADDRESS])
    print(t)


def emplist():
    headers = ['Selected Option']
    table = [['Teacher Details']]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    mycursor.execute("select* from teacher")
    results = mycursor.fetchall()
    t = PrettyTable(['TEACHER_ID', 'TEACHER_NAME', 'TEACHER_DEPT', 'TEACHER_NO', 'TEACHER_AGE'])
    for TEACHER_ID, TEACHER_NAME, TEACHER_DEPT, TEACHER_NO, TEACHER_AGE in results:
        t.add_row([TEACHER_ID, TEACHER_NAME, TEACHER_DEPT, TEACHER_NO, TEACHER_AGE])
    print(t)
