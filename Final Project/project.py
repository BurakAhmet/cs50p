from abc import ABC
from tabulate import tabulate
import re
import sys


class School(ABC):  # Abstract class
    @property
    def school_name(self) -> str:
        return self.__school_name

    @school_name.setter
    def school_name(self, name):
        if not name:
            raise ValueError("Missing name")
        self.__school_name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self.__name = name

    @staticmethod
    def show_all(lst):
        if lst:
            print(tabulate(lst, headers="keys", tablefmt="grid"))
        else:
            print("\nThe list is empty.")


class Student(School):
    __total_student = 0
    students = []

    def __init__(self, name, department, school_name):
        self.name = name
        self.__department = department
        Student.__total_student += 1
        self.__id = Student.__total_student
        self.school_name = school_name
        Student.students.append({"ID": self.__id, "Name": name, "Department": department, "School Name": school_name})

    def __str__(self):
        return f"{self.__id} {self.name} {self.__department} {self.school_name}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def visa(self) -> int:
        return self.__visa

    @visa.setter
    def visa(self, score: int):
        if score < 0:
            raise Exception("Score value must be equal or greater than zero")
        self.__visa = score

    @property
    def final(self) -> int:
        return self.__final

    @final.setter
    def final(self, score: int):
        if score < 0:
            raise Exception("Score value must be equal or greater than zero")
        self.__final = score

    @property
    def average_score(self) -> float | None:
        if self.__visa and self.__final:
            return self.__visa * 40 / 100 + self.__final * 60 / 100
        return None

    @property
    def letter_grade(self) -> str | None:
        if not self.average_score:
            return None
        if self.average_score >= 85:
            return "AA"
        elif self.average_score >= 75:
            return "BA"
        elif self.average_score >= 65:
            return "BB"
        elif self.average_score >= 55:
            return "CB"
        elif self.average_score >= 45:
            return "CC"
        elif self.average_score >= 35:
            return "DC"
        elif self.average_score >= 25:
            return "DD"
        elif self.average_score >= 15:
            return "FD"
        else:
            return "FF"


class Employee(School):
    employees = []

    def __init__(self, title, name, school_name, password):
        self.__title = title
        self.name = name
        self.school_name = school_name
        self.__password = password
        Employee.employees.append({"Title": title, "Name": name, "School": school_name, "Password": password})

    def __str__(self):
        return f"{self.__title} {self.name} {self.school_name}"

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


def main():
    print("*---Welcome!---*")
    while True:
        match select_action():
            case 0:
                sys.exit("Exited.")
            case 1:
                if employee_login():
                    emp_page_process = employee_page()
                    while emp_page_process != 0:
                        match emp_page_process:
                            case 0: break
                            case 1: create_student()
                            case 2: Student.show_all(Student.students)
                            case 3: Employee.show_all(Employee.employees)
                        emp_page_process = employee_page()
            case 2:
                employee_register()


def select_action() -> int:
    print("1-Employee login\n"
          "2-Register\n"
          "0-Exit\n")
    return take_valid_interval("Select the action you want to take: ", 0, 2)


def employee_login() -> bool:  # returns True if username and password is correct
    username = input("Username: ")
    password = input("Password: ")
    for emp in Employee.employees:
        if emp["Name"] == username and emp["Password"] == password:
            print("Logged in.")
            return True
    print("Your username or password is wrong!\n")


def employee_register() -> Employee:
    title = take_input_until_valid_title("Title: ")
    name = take_input_until_valid_name("Name: ")
    school = input("School: ")
    password = take_input_until_valid_password("Password (Your password must be contains at least 1 letter 1 number and 5 characters): ")
    print("Successfully registered.\n")
    return Employee(title, name, school, password)


def employee_page() -> int:
    print("\n1-Create new student\n"
          "2-Show all students\n"
          "3-Show all employees\n"
          "0-Back\n")
    return take_valid_interval("Select the action you want to take: ", 0, 3)


def create_student() -> Student:
    name = take_input_until_valid_name("Name: ")
    department = input("Department: ")
    school = input("School: ")
    student = Student(name, department, school)
    student.visa = take_valid_interval("Visa score: ", 0, 100)
    student.final = take_valid_interval("Final Score: ", 0, 100)
    Student.students[student.id - 1].update({"Visa": student.visa, "Final": student.final,
                                             "Average Score": student.average_score, "Letter Grade": student.letter_grade})
    print("Student created.\n")
    return student


def take_input_until_valid_name(prompt: str) -> str:
    while True:
        name = input(prompt)
        if validate_name(name):
            return name
        print("Your name can not include numbers or symbols! Enter again.")


def take_input_until_valid_password(prompt: str) -> str:
    while True:
        password = input(prompt)
        if validate_password(password):
            return password
        print("Invalid password! Enter again.")


def take_input_until_valid_title(prompt: str) -> str:
    while True:
        title = input(prompt)
        if validate_title(title):
            return title
        print("Your title can not include symbols and can not be shorter than 3 character and can not be longer than 5 character! Enter again.")


def take_valid_interval(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        selection = take_int(prompt)
        if min_val <= selection <= max_val:
            return selection
        else:
            print(f"\nPlease enter a number between {min_val} - {max_val}!")


def take_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please use integer only!")
            pass


def validate_title(title):
    if re.search(r"^[a-zA-Z]{3,4}$", title):
        return True
    return False


def validate_password(password: str) -> bool:
    if re.search(r"^(?=.*\d)(?=.*[a-zA-Z]).{5,}$", password):
        return True
    return False


def validate_name(name: str) -> bool:
    if re.search(r"^[a-zA-Z]+(?:\s[a-zA-Z]+)*$", name):
        return True
    return False


if __name__ == "__main__":
    main()
