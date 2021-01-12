import sys

import matplotlib.pyplot as plt
import mysql.connector as sql
import prettytable
from prettytable.prettytable import PrettyTable
from tabulate import tabulate

conn = sql.connect(host='localhost', user='root', password='1234', database='project')
mycursor = conn.cursor()


def student():
    while True:
        std_table = [[1, "TP MARK"], [2, "Student Details"], [3, "AVERAGE  MARK"], [4, 'YEARLY PERFORMANCE'],
                     [0, 'Go Back To Main Menu'], ['*', 'EXIT']]
        std_headers = ['Students Menu']
        print(tabulate(std_table, std_headers, tablefmt="fancy_grid", floatfmt=".1f"))
        std_choice: str or int = input('Enter Your Choice: ').capitalize()
        if std_choice == '1' or std_choice == 'SUBJECT MARK':
            submark()
        elif std_choice == '2' or std_choice == 'MARKLIST':
            stddetails()
        elif std_choice == '3' or std_choice == 'AVERAGE  MARK':
            avgmark()
        elif std_choice == '4' or std_choice == 'YEARLY PERFORMANCE':
            yearlyperformance()
        elif std_choice == '*' or std_choice == 'EXIT':
            print("Thank You")
            sys.exit()
        elif std_choice == '0' or std_choice == ' Go Back To Main Menu':
            break
        else:
            print('Enter A Valid Option')


def sqlprint():
    results = mycursor.fetchall()
    t = prettytable.PrettyTable(['STD_ID', 'STD_NAME', 'ENGLISH', 'MALAYALAM', 'MATHS', 'BIOLOGY', 'CHEMISTRY',
                                 'PHYSICS'])
    for STD_ID, STD_NAME, ENGLISH, MALAYALAM, MATHS, BIOLOGY, CHEMISTRY, PHYSICS in results:
        t.add_row([STD_ID, STD_NAME, ENGLISH, MALAYALAM, MATHS, BIOLOGY, CHEMISTRY, PHYSICS])
    print(t)


def submark():
    stdid = int(input("Enter The Student Id: "))
    table = [[1, "Test Paper 1"], [2, "Test Paper 2"], [3, 'Test Paper 3'], [4, 'Test Paper 4']]
    headers = ["Conducted Exams"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    exam = input('Select The Tp: ')

    if exam == '1':
        mycursor.execute(" select * from tp1 where STD_ID= '{}' ".format(stdid))
        sqlprint()
    elif exam == '2':
        mycursor.execute(" select * from tp2 where STD_ID= '{}' ".format(stdid))
        sqlprint()
    elif exam == '3':
        mycursor.execute(" select * from tp3 where STD_ID= '{}' ".format(stdid))
        sqlprint()
    elif exam == '4':
        mycursor.execute(" select * from tp4 where STD_ID= '{}' ".format(stdid))
        sqlprint()
    else:
        print('Wrong Option')


def stddetails():
    stdid = int(input('Enter The Student Id: '))
    mycursor.execute("select * from students where STD_ID='{}'".format(stdid))
    results = mycursor.fetchall()
    t = PrettyTable(['STD_ID', 'STD_NAME', 'STD_GRADE', 'STD_AGE', 'STD_NUMBER', 'STD_ADDRESS'])
    for STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER, STD_ADDRESS in results:
        t.add_row([STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER, STD_ADDRESS])
    print(t)


def avgmark():
    stdid = int(input('Enter Your Student ID: '))
    table = [[1, "Test Paper 1"], [2, "Test Paper 2"], [3, 'Test Paper 3'], [4, 'Test Paper 4'],
             ]
    headers = ["Conducted Exams"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    exam = input('Select The TP: ')
    if exam == '1':
        mycursor.execute(
            "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100  from tp1 where STD_ID='{}'".format(
                stdid))
        x = mycursor.fetchone()
        print('Your Average Mark For TP 1 is:', x[0])

    elif exam == '2':
        mycursor.execute(
            "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp2 where STD_ID='{}'".format(
                stdid))
        x = mycursor.fetchone()
        print('Your Average Mark For TP 2 is:', x[0])
    elif exam == '3':
        mycursor.execute(
            "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp3 where STD_ID='{}'".format(
                stdid))
        x = mycursor.fetchone()
        print('Your Average Mark For TP 3 is:', x[0])
    elif exam == '4':
        mycursor.execute(
            "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp4 where STD_ID='{}'".format(
                stdid))
        x = mycursor.fetchone()
        print('Your Average Mark For TP 4 is:', x[0])

    else:
        print('Wrong Option')


def yearlyperformance():
    stdid = int(input('Enter Your Student ID: '))
    mycursor.execute(
        "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100  from tp1 where STD_ID='{}'".format(
            stdid))
    x1 = mycursor.fetchone()
    mycursor.execute(
        "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp2 where STD_ID='{}'".format(
            stdid))
    x2 = mycursor.fetchone()
    mycursor.execute(
        "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp3 where STD_ID='{}'".format(
            stdid))
    x3 = mycursor.fetchone()
    mycursor.execute(
        "select  (ENGLISH+MALAYALAM+Maths+BIOLOGY+CHEMISTRY+PHYSICS)*6/100 from tp4 where STD_ID='{}'".format(
            stdid))
    x4 = mycursor.fetchone()
    x = [x1[0], x2[0], x3[0], x4[0]]
    y = ['Tp1', 'Tp2', 'Tp3', 'Tp4']
    plt.plot(y, x, marker='*')
    plt.xlabel('Marks')
    plt.ylabel('Test Papers')
    plt.show()
