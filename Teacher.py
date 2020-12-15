import mysql.connector as sql
from tabulate import tabulate
from prettytable import PrettyTable
conn = sql.connect(host='localhost', user='root', password='1234', database='project')
mycursor = conn.cursor()


def sqlprint():
    results = mycursor.fetchall()
    t = PrettyTable(['STD_ID', 'STD_NAME', 'ENGLISH', 'MALAYALAM', 'MATHS', 'BIOLOGY', 'CHEMISTRY', 'PHYSICS'])
    for STD_ID, STD_NAME, ENGLISH, MALAYALAM, MATHS, BIOLOGY, CHEMISTRY, PHYSICS in results:
        t.add_row([STD_ID, STD_NAME, ENGLISH, MALAYALAM, MATHS, BIOLOGY, CHEMISTRY, PHYSICS])
    print(t)



def teacher():
    while True:
        tea_table = [[1, "STUDENT LIST"], [2, "STUDENT DETAILS"], [3, 'MARKLIST'], [4, 'CLASS AVERAGE'],
                     [5, 'ADD TP MARKS'], [6,'Conduct A New Tp'],[0, 'GO BACK TO THE MAIN MENU']]
        tea_headers = ['Teacher Menu']
        print(tabulate(tea_table, tea_headers, tablefmt="fancy_grid", floatfmt=".1f"))
        choice: str or int = input('Enter Your Choice')
        if choice == '1' or choice == 'STUDENT LIST':
            stdlist()
        elif choice == '2' or choice == 'STUDENT DETAILS':
            stddetails()
        elif choice == '3' or choice == 'MARKLIST':
            marklist()
        elif choice == '4' or choice == 'CLASS AVERAGE':
            classaverage()
        elif choice == '5' or choice == 'ADD TP MARKS':
            updatemarklist()
        elif choice == '0' or choice == ' GO BACK TO THE MAIN MENU':
            break


def stdlist():
    headers = ['Selected Option']
    table = [['Student List']]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    mycursor.execute("select * from students")
    results = mycursor.fetchall()
    t = PrettyTable(['STD_ID', 'STD_NAME', 'STD_GRADE', 'STD_AGE', 'STD_NUMBER'])
    for STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER in results:
        t.add_row([STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER])
    print(t)



def stddetails():
    stdid = int(input('Enter The Student Id'))
    mycursor.execute("select * from students where STD_ID='{}'".format(stdid))
    results = mycursor.fetchall()
    t = PrettyTable(['STD_ID', 'STD_NAME', 'STD_GRADE', 'STD_AGE', 'STD_NUMBER'])
    for STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER in results:
        t.add_row([STD_ID, STD_NAME, STD_GRADE, STD_AGE, STD_NUMBER])
    print(t)



def marklist():
    table = [[1, "Test Paper 1"], [2, "Test Paper 2"], [3, 'Test Paper 3'], [4, 'Test Paper 4']]
    headers = ["Conducted Exams"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    exam = input('Select The Tp')
    if exam == '1':
        mycursor.execute("select * from tp1")
        sqlprint()
    elif exam == '2':
        mycursor.execute("select * from tp2")

        sqlprint()
    elif exam == '3':
        mycursor.execute("select * from tp3")
        sqlprint()
    elif exam == '4':
        mycursor.execute("select * from tp4")
        sqlprint()
    else:
        print('Wrong Option')


def classaverage():
    table = [[1, "Test Paper 1"], [2, "Test Paper 2"], [3, 'Test Paper 3'], [4, 'Test Paper 4']]
    headers = ["Conducted Exams"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    exam = input('Select The TP')
    if exam == '1':
        mycursor.execute(
            "select  STD_ID, STD_NAME, avg(ENGLISH), avg(MALAYALAM) , avg(Maths) , avg(BIOLOGY) , "
            "avg(CHEMISTRY), avg(PHYSICS)  from tp1")
        sqlprint()
    elif exam == '2':
        mycursor.execute(
            "select  STD_ID, STD_NAME, avg(ENGLISH) as English, avg(MALAYALAM) as Malayalam, avg(Maths) as Maths,"
            " avg(BIOLOGY) as Biology,"
            " avg(CHEMISTRY) as Chemistry, avg(PHYSICS) as Physics from tp2")
        sqlprint()
    elif exam == '3':
        mycursor.execute(
            "select STD_ID, STD_NAME,  avg(ENGLISH) as English, avg(MALAYALAM) as Malayalam, avg(Maths) as Maths,"
            " avg(BIOLOGY) as Biology,"
            " avg(CHEMISTRY) as Chemistry, avg(PHYSICS) as Physics from tp3")
        sqlprint()
    elif exam == '4':
        mycursor.execute(
            "select  STD_ID, STD_NAME, avg(ENGLISH) as English, avg(MALAYALAM) as Malayalam, avg(Maths) as Maths, "
            "avg(BIOLOGY) as Biology,"
            " avg(CHEMISTRY) as Chemistry, avg(PHYSICS) as Physics from tp4")
        sqlprint()
    else:
        print('Wrong Option')


def updatemarklist():
    table = [[1, "Test Paper 1"], [2, "Test Paper 2"], [3, 'Test Paper 3'], [4, 'Test Paper 4']]
    headers = ["Conducted Exams"]
    print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
    exam = input('Select The TP')
    if exam == '1':
        STD_ID = int(input("Enter The Student Id: "))
        STD_NAME = input("Enter the Name: ")
        ENGLISH = int(input('Enter the mark for Engish'))
        MALAYALAM = int(input('Enter the mark for Malayalam'))
        MATHS = int(input('Enter the mark for Maths'))
        BIOLOGY = int(input('Enter the mark for Biology'))
        CHEMISTRY = int(input('Enter the mark for Chemistry'))
        PHYSICS = int(input('Enter the mark for Physics'))
        mycursor.execute(
            "insert into tp1 values('{}','{}', '{}', '{}','{}', '{}', '{}','{}')".format(STD_ID, STD_NAME, ENGLISH,
                                                                                         MALAYALAM, MATHS, BIOLOGY,
                                                                                         CHEMISTRY, PHYSICS))
        conn.commit()
    elif exam == '2':
        STD_ID = int(input("Enter The Student Id: "))
        STD_NAME = input("Enter the Name: ")
        ENGLISH = int(input('Enter the mark for Engish'))
        MALAYALAM = int(input('Enter the mark for Malayalam'))
        MATHS = int(input('Enter the mark for Maths'))
        BIOLOGY = int(input('Enter the mark for Biology'))
        CHEMISTRY = int(input('Enter the mark for Chemistry'))
        PHYSICS = int(input('Enter the mark for Physics'))
        mycursor.execute(
            "insert into tp2 values('{}','{}', '{}', '{}','{}', '{}', '{}','{}')".format(STD_ID, STD_NAME, ENGLISH,
                                                                                         MALAYALAM, MATHS, BIOLOGY,
                                                                                         CHEMISTRY, PHYSICS))
        conn.commit()
    elif exam == '3':
        STD_ID = int(input("Enter The Student Id: "))
        STD_NAME = input("Enter the Name: ")
        ENGLISH = int(input('Enter the mark for Engish'))
        MALAYALAM = int(input('Enter the mark for Malayalam'))
        MATHS = int(input('Enter the mark for Maths'))
        BIOLOGY = int(input('Enter the mark for Biology'))
        CHEMISTRY = int(input('Enter the mark for Chemistry'))
        PHYSICS = int(input('Enter the mark for Physics'))
        mycursor.execute(
            "insert into tp3 values('{}','{}', '{}', '{}','{}', '{}', '{}','{}')".format(STD_ID, STD_NAME, ENGLISH,
                                                                                         MALAYALAM, MATHS, BIOLOGY,
                                                                                         CHEMISTRY, PHYSICS))
        conn.commit()
    elif exam == '4':
        STD_ID = int(input("Enter The Student Id: "))
        STD_NAME = input("Enter the Name: ")
        ENGLISH = int(input('Enter the mark for Engish'))
        MALAYALAM = int(input('Enter the mark for Malayalam'))
        MATHS = int(input('Enter the mark for Maths'))
        BIOLOGY = int(input('Enter the mark for Biology'))
        CHEMISTRY = int(input('Enter the mark for Chemistry'))
        PHYSICS = int(input('Enter the mark for Physics'))
        mycursor.execute(
            "insert into tp4 values('{}','{}', '{}', '{}','{}', '{}', '{}','{}')".format(STD_ID, STD_NAME, ENGLISH,
                                                                                         MALAYALAM, MATHS, BIOLOGY,
                                                                                         CHEMISTRY, PHYSICS))
        conn.commit()
    else:
        print('Wrong Option')
