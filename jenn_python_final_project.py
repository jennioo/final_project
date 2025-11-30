Title = """FINAL PROJECT: SCHOOL MANAGEMENT SYSTEM (BEGINNER LEVEL)
Project Description:
You will build a simple School Management System that demonstrates everything you have learned so far
"""
jenn_schools = """
 .................:-+#*....-#%%%%%##-...:*#--:................. 
 ................=:#*:...*%%*####*+*%%+...-*#:=................ 
 ...............-+*=........*%%%%##+........+#+-............... 
 ..............:##+.........=*#%%#+-.........*#*............... 
 .............:##*.......-#%%%+..*%%%#:.......###.............. 
 .............=**-....:+%#%%%%%##%%%%%#%=:....-+*=............. 
 .............-+=:....##%#%%%%%%#%%%%%#%#+....:---............. 
 .............:=::....##%#%%%%%%#%%%%%#%#+....::-:............. 
 ..............=-.....##%#%%%%%%#%%%%%#%#+.....++.............. 
 .............:*#-:...##%#%%%%%%#%%%%%#%#+....=#*.............. 
 ..............:##-:..##%#****####****#%#+...+##:.............. 
 ...............:*#=-.+********--********=.:+*+:............... 
 ...........:.....+#%--..................--#*-................. 
 ...........#%%%%#*:+##:...:--::----:...:%#=:*#%%%%+........... 
 ...........#%%*###=--:::::...........::::--=##*=%%+........... 
 ............:=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%==:............ 
 ..............*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%-.............. 
 ...............::::------===========-------::::...............                                                               
"""

import random
student_list = []

def subjects():   
    subjects= ["Mathematics", "English Language", "Physics", "Chemistry", "Biology","Computer Science", "Economics", "Geography", "History", "Government", "Literature", "Civic Education", "Agricultural Science", "Religious Studies", "Fine Arts"]
    return random.sample(subjects, 8)

def grades():
    return random.randint(1,100)
            

class Student():
    def __init__(self, fname, lname, age, subjects =None,grades=None):
        self.fname = fname.lower().strip()
        self.lname = lname.lower().strip()
        self.age = age
        self.subjects = subjects if subjects else {}
        self.grades = grades if grades else []


    def add_subject(self, subject_name, grade):
        self.subjects[subject_name] = grade


    def add_grade(self):
        return random.randint(1, 100)

    def average_grade(self):
            if not self.subjects:       
                return 0
            return sum(self.subjects.values()) / len(self.subjects)
    def overall_average(self):
        if not self.subjects:
            return 0
        return sum(self.subject.values() / len(self.subjects))

    def passed(self):
        return self.average_grade() >= 50

    def summary(self):
        print(f"\n=== Student Report ===")
        print(f"Name: {self.fname.capitalize()} {self.lname.capitalize()}")
        print(f"Age: {self.age}")
        print(f"\nSubjects and Grades:")

        if not self.subjects:
            print("  No subjects registered")
        else:
            for subject, grade in self.subjects.items():
                print(f"  {subject}: {grade}")
        
        print(f"\nAverage: {self.average_grade():.2f}")
        print("Status:", "PASSED " if self.passed() else "FAILED ")

 

try:
    with open("all_students.txt") as file:
         for line in file:
            line = line.strip()
            
            if not line:
                continue
            
            parts = [p.strip().replace('"','') for p in line.split(",")]
            if not parts[0]:
                continue
            full_name = parts[0]
            
            name_parts = full_name.split()
            fname = name_parts[0]
            lname = name_parts[1] if len(name_parts) > 1 else ""

            if len(parts) > 1 and parts[1].isdigit():
                age = int(parts[1])
                subject_start_index = 2
            else:
                age = 0  
                subjects_start_index = 1

            
            new_student = Student(fname, lname, age)
            for sg in parts[subject_start_index:]:
                if ":" in sg:
                    subject, grade = sg.split(":")
                    new_student.add_subject(subject, int(grade))

            student_list.append(new_student)
        
    print(f"Loaded {len(student_list)} students from file\n")
except FileNotFoundError:
    print(" No student file found, starting with empty list\n")       

      

print("Welcome to the Student Management System of jenn_schools")
print("Our motto: Integrity andKnowledge")
print("Enter your username and passcode to login")
username =str(input("Username >>")).lower().strip()
passcode = int(input("Passcode >>"))

right_username = "Nonso"
right_passcode = 1234

while True:
    if not username == right_username and not passcode == right_passcode:
        print("You have inputed wrongly, try again")
        print(username =str(input("Username >>")).lower().strip())
        print(passcode = int(input("Passcode >>")))
    else:
        print("You have logged in successfully")
        break

while True:
    menu = print("\n--THE MENU SYSTEM--")
    
    print("""
1. Add a new student
2. Add grades to a student
3. View student report
4. View all students
5. Ranking student average
6. Exit
    """)
        
    print("what do you intend to do?")
    menu_choice = int(input("Select using numbers:"))

    if menu_choice == 1:
        print("\n**ADD A NEW STUDENT**")
        new_student_fname =str(input("First_name:")).lower().strip()
        new_student_lname =str(input("Last_name:")).lower().strip ()
        new_student_age =int(input("Age:"))

        new_student = Student(new_student_fname, new_student_lname, new_student_age)
        student_list.append(new_student)
        print(f" Student {new_student_fname.capitalize()} {new_student_lname.capitalize()} added successfully!")
 

    elif menu_choice == 2:
         print("\n**ADD GRADE TO STUDENT**")
         grade_fname = input("Enter student first name: ").lower().strip()
         grade_lname = input("Enter student last name: ").lower().strip()
         

         found = False
         for s in student_list:
            print(f"Checking: '{s.fname}' == '{grade_fname}' and '{s.lname}' == '{grade_lname}'")  # DEBUG
            if s.fname == grade_fname and s.lname == grade_lname:
                found = True

            print("\nAvailable subjects:")
            available_subjects = ["Mathematics", "English Language", "Physics", "Chemistry", 
                            "Biology", "Computer Science", "Economics", "Geography", 
                            "History", "Government", "Literature", "Civic Education", 
                            "Agricultural Science", "Religious Studies", "Fine Arts"]
        
            for i  in available_subjects:
                print(i)
            print()

            num_subjects = int(input("How many subjects are you adding grades for? "))
            
            for i in range(num_subjects):
                print(subjects)
                subject_name = input(f"Enter subject {i+1} Name: ").strip()
                grade = int(input(f"Enter grade for {subject_name} (1-100): "))
                
                
                s.add_subject(subject_name, grade)
            
            print(f"Added {num_subjects} subjects with grades!")
            break

         if not found:
            print(" Student not found")

    elif menu_choice == 3:
        print("\n**VIEW STUDENT REPORT**")
        report_fname =str(input("first_name:")).lower().strip()
        report_lname =str(input("last_name:")).lower().strip()
        found = False
        for s in student_list:
            if s.fname == report_fname and s.lname == report_lname:
                found = True
                s.summary()
                break

        if not found:
            print(f"No student by the name {report_fname} {report_lname}")
       
                    

    elif menu_choice == 4:
            print("\n**VIEW ALL STUDENTS**")
            if not student_list:
                    print("No students available")
            else:
                 num = 1
                 for s in student_list:
                        print(f"{num}. {s.fname.capitalize()} {s.lname.capitalize()}")
                        num += 1

    elif menu_choice == 5:
        print("\n**STUDENT RANKINGS BY AVERAGE**")
        if len(student_list) == 0:
            print("No students available")
     
        else:
            ranked_students = []
        
            for s in student_list:
                avg = s.average_grade()
                if avg > 0:
                    ranked_students.append([s.fname, s.lname, avg])
            
            if len(ranked_students) == 0:
                print("No students have grades yet")
            
            else:
                for i in range(len(ranked_students)):
                    for j in range(len(ranked_students) - 1):
                        if ranked_students[j][2] < ranked_students[j + 1][2]:
                            temp = ranked_students[j]
                            ranked_students[j] = ranked_students[j + 1]
                            ranked_students[j + 1] = temp
                
                print("\n=== RANKINGS ===")
                print("Rank , Name , Average")
                print("-" * 40)
                
                rank = 1
                for student in ranked_students:
                    fname = student[0].capitalize()
                    lname = student[1].capitalize()
                    avg = student[2]
                    
                    print(f"{rank}. {fname} {lname} - {avg:.2f}")
                    rank = rank + 1
                            

    elif menu_choice == 6:
            print("Goodbye")
            break

    else:
        print("Invalid choice try again")          

