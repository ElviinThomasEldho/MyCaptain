from csv import writer, reader

def inputData():
    print("Enter Student Details")
    rno = input("Roll Number : ")
    name = input("Full Name   : ")
    grade = input("Grade       : ")
    print("Marks in Subjects (Out of 100) :-")
    m1 = int(input("1. Subject 1 : "))
    m2 = int(input("2. Subject 2 : "))
    m3 = int(input("3. Subject 3 : "))
    m4 = int(input("4. Subject 4 : "))
    m5 = int(input("5. Subject 5 : "))

    mo = (m1 + m2 + m3 + m4 + m5)/5

    if mo >= 90:
        grd = 'A'
    elif mo >= 80:
        grd = 'B'
    elif mo >= 70:
        grd = 'C'
    elif mo >= 60:
        grd = 'D'
    elif mo >= 50:
        grd = 'E'
    elif mo >= 40:
        grd = 'F'

    print("Overall Grade : ",grd)

    studentData = [rno,name,grade,m1,m2,m3,m4,m5,grd]

    with open('studentDB.csv', 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(studentData)

def viewData():
    with open('studentDB.csv','rt')as f:
      data = reader(f)
      i=1
      for row in data:
            print("Student ",i)
            print("Roll Number : ",row[0])
            print("Full Name : ",row[1])
            print("Grade : ",row[2])
            print("Marks in Subjects")
            print("Subject 1 : ",row[3])
            print("Subject 2 : ",row[4])
            print("Subject 3 : ",row[5])
            print("Subject 4 : ",row[6])
            print("Subject 5 : ",row[7])
            print("Overall Grade : ",row[8])
            i += 1

if __name__ == "__main__":
    opt = 0;
    while opt != 3:
        print("Main Menu :-")
        print("1. Enter Student Record")
        print("2. View Student Records")
        print("3. Exit")
        opt = int(input("Select Option : "))
        if opt == 1:
            inputData()
        elif opt == 2:
            viewData()
        else:
            break

'''
Output :
Main Menu :-
1. Enter Student Record
2. View Student Records
3. Exit
Select Option : 2
Student  1
Roll Number :  12
Full Name :  Elviin Thomas Eldho
Grade :  12
Marks in Subjects
Subject 1 :  98
Subject 2 :  99
Subject 3 :  98
Subject 4 :  99
Subject 5 :  98
Overall Grade :  A
Main Menu :-
1. Enter Student Record
2. View Student Records
3. Exit
Select Option : 1
Enter Student Details
Roll Number : 10
Full Name   : Eedwinn Eldho
Grade       : 9
Marks in Subjects (Out of 100) :-
1. Subject 1 : 78
2. Subject 2 : 87
3. Subject 3 : 98
4. Subject 4 : 89
5. Subject 5 : 100
Overall Grade :  A
Main Menu :-
1. Enter Student Record
2. View Student Records
3. Exit
Select Option : 3

'''
