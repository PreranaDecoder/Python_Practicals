# Define a class person (attributes:\tname, department, date Of Birth).
# Derive two classes employee(attributes:\temployee id, sal) and
# student(attributes:\tPRN, year, CGPA) from person class.
# Derive two classes lab_assistant(attributes:\tlabs) and
# faculty(attributes:\tsubject, number of research papers, qualification).
# i) Create objects for lab assistant, faculties, and students.
# ii) Display the data.
# iii) Delete a data
# iv) Find the total sal of all employees.
# v) Find average CGPA of students department wise.

class person:
    def __init__(self, name, dept, dob):
        self.name = name
        self.dept = dept
        self.dob = dob

    def __str__(self):
        print('Name:\t', self.name)
        print('Department:\t', self.dept)
        print('Date of birth:\t', self.dob)
        print("")

    def delete(self):
        print("Data deleted for", self.name)
        del self
        print()


class employee(person):
    total_sal = 0

    def __init__(self, name, dept, dob, id, sal):
        super().__init__(name, dept, dob)
        self.id = id
        self.sal = sal
        employee.total_sal += sal

    def totalsal():
        print("Total salary of all employees: Rs.", employee.total_sal)
        print("")

    def display(self):
        print(self.id, '\t', self.name, '\t',
              self.dep, '\t', self.dob, '\t', self.sal)

    def __str__(self):
        print('Name:\t', self.name)
        print('Department:\t', self.dept)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\tRs.', self.sal)
        print("")


class lab_assistant(employee):
    def __init__(self, name, dept, dob, id, sal, labs):
        super().__init__(name, dept, dob, id, sal)
        self.labs = labs

    def display(self):
        print(self.id, '\t', self.name, '\t', self.dept, '\t',
              self.dob, '\tRs.', self.sal, '\t', self.labs)

    def __str__(self):
        print('Faculty name:\t', self.name)
        print('Department:\t', self.dept)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\t\tRs.', self.sal)
        print('Labs:\t', self.labs)


class faculty(employee):
    def __init__(self, name, dept, dob, id, sal, sub, no_rsp, qual):
        super().__init__(name, dept, dob, id, sal)
        self.sub = sub
        self.no_rsp = no_rsp
        self.qual = qual

    def display(self):
        print(self.id, '\t', self.name, '\t', self.dept, '\t', self.dob, '\tRs.',
              self.sal, '\t', self.sub, '\t\t', self.no_rsp, '\t\t\t', self.qual)

    def __str__(self):
        print('Faculty name:\t', self.name)
        print('Department:\t', self.dept)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\t\tRs.', self.sal)
        print('Subject:\t', self.sub)
        print('No. of research papers:\t', self.no_rsp)
        print('Qualifications:\t', self.qual)
        print()


class student(person):
    comp_cgpa, it_cgpa, mech_cgpa = 0, 0, 0
    comp, it, mech = 0, 0, 0

    def __init__(self, name, dept, dob, prn, yr, cgpa):
        super().__init__(name, dept, dob)
        self.prn = prn
        self.yr = yr
        self.cgpa = cgpa
        if dept == "Computer":
            student.comp_cgpa += cgpa
            student.comp += 1
        elif dept.strip() == "IT":
            student.it_cgpa += cgpa
            student.it += 1
        elif dept == "Mechanical":
            student.mech_cgpa += cgpa
            student.mech += 1

    def avg_cgpa():
        print("Average CGPA of students department-wise : ")
        print("Computer : \t", student.comp_cgpa/student.comp)
        print("IT : \t\t", student.it_cgpa/student.it)
        print("Mechanical : \t", student.mech_cgpa/student.mech)
        print()

    def display(self):
        print(self.prn, '\t', self.name, '\t', self.dept, '\t',
              self.dob, '\t', self.yr, '\t\t', self.cgpa)

    def __str__(self):
        print('Student name : \t', self.name)
        print('Department : \t', self.dept)
        print('Date of Birth : \t', self.dob)
        print('PRN : \t', self.prn)
        print('Year : \t', self.yr)
        print('CGPA : \t', self.cgpa)
        print()

# i) Create objects for lab assistant, faculties, and students.


l1 = lab_assistant("Rohan Deshmukh", "Computer",
                   "13/4/1982", "3035", 20000, "OS")
l2 = lab_assistant("Riyansh Patil", "Computer",
                   "23/7/1985", "3482", 18000, "Python")
l3 = lab_assistant("Bhavika Patel", "Computer",
                   "4/12/1985", "3062", 19000, "DAA")

lab = [l1, l2, l3]

f1 = faculty("Paresh Vaity", "Computer", "13/5/1978",
             "5411", 90000, "OS\t", 5, "PhD")
f2 = faculty("Pranav Patil","Computer", "27/6/1981",
             "2465", 70000, "Python", 4, "M.Tech")
f3 = faculty("Shreya Ghosh", "Computer", "16/1/1988",
             "1254", 60000, "DAA\t", 3, "M.Tech")

fac = [f1, f2, f3]

s1 = student("Ruchi Patil", "Computer", "7/2/2003",
             "2130331245000", "1st", 8.77)
s2 = student("Tushar Tare", "Computer", "26/8/2002",
             "2030331245034", "2nd", 9.67)
s3 = student("Aruna Bhoir", "Computer", "15/4/2001",
             "1930331245076", "3rd", 7.72)
s4 = student("Krish Arora", "Computer", "2/5/1999",
             "1830331245011", "4th", 8.23)
s5 = student("Rajesh Birla", "IT\t", "5/6/2003",
             "2130331245021", "1st", 9.27)

students = [s1, s2, s3, s4, s5]


# ii) Display the data.
print("Employees:")
print("Lab assistants:")
print('ID\t', 'Name\t\t', 'Department\t',
      'Date of birth\t', 'Salary\t\t', 'Labs\t')
for i in lab:
    i.display()
print()


print("Faculty:")
print('ID\t', 'Name\t\t', 'Department\t', 'Date of birth\t', 'Salary\t\t',
      'Subject\t', 'No. of research papers\t', 'Qualification')
for i in fac:
    i.display()
print()


print("Students:")
print('PRN\t\t', 'Name\t\t', 'Department\t',
      'Date of birth\t', 'Year\t\t', 'CGPA\t')
for i in students:
    i.display()
print()


# iii) Delete a data
s1.delete()
f2.delete()


# iv) Find the total sal of all employees.
print(employee.totalsal())


# v) Find average CGPA of students department wise.
print(student.avg_cgpa())