def write_record(info_list,num):
    f = open("Student_Record.txt",'a')
    f.write("\nStudent Number : "+str(num))
    f.write("\nName : "+str(info_list[0]))
    f.write("\nAge : "+str(info_list[1]))
    f.write("\nContact Number : "+str(info_list[2]))
    f.write("\nE-mail ID : "+str(info_list[3]))
    f.close()

if __name__ == '__main__':
    condition = True
    student_num = 1

    while (condition):
        student_info = input("Enter some student #{} information (Name Age Contact_Number Email_ID) : ".format(student_num))
        print("Entered information",student_info)

        #split
        student_info_list = student_info.split(" ")
        print("Entered split up information : ",str(student_info_list))

        print("\nThe entered information is -\nName : {}\nAge : {}\nContact Number : {}\nE-mail ID : {}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered information correct? (yes/no)")

        if choice_check == "yes":
            write_record(student_info_list,student_num)
            condition_check = input("Enter (yes/no) if you want to enter for another student:")
            if(condition_check == "yes"):
                condition = True
                student_num += 1
            elif (condition_check == "no"):
                condition = False
        elif choice_check == "no":
            print("Please re-enter the values")


