# Basic school administration tool
import csv

def writeIntoCsv(info_list):
    with open("student_info.csv", 'a', newline='') as csv_file:  #w+ = write mode in csv, a= append in csv
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","E-mail ID"])
        
        writer.writerow(info_list)

if __name__ == '__main__':
    condition=True
    student_num=1

    while(condition):
        student_info=input("Enter student information for student #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num))

    
        #split
        student_info_list= student_info.split(" ")

        print("\n The entered Info is: \nName: {}\nAge: {}\nContact_Number: {}\nEmail_ID: {}"
                .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_chk=input("Is the entered info correct ? (yes/no): ")
        if choice_chk == "yes":
            writeIntoCsv(student_info_list)
            
            condition_check= input("Enter (yes/no) if you want to enter information of another student: ")
            if condition_check == "yes":
                    condition=True
                    student_num+=1
            elif condition_check == "no":
                    condition=False
        elif choice_chk == "no":
            print("\n Please re-enter the values!")