    # STUDENT AUTOMATİON
    #### Video Demo:  <https://youtu.be/4cLC1nAPFx4>
    #### Description:
    At the first a greeting page is welcome us and wants a action to take.
    If you haven't registered already and if you try to login you can not login becaue you don't have username and password so you need to be register first.
    If you enter something you shouldn't have done then program warns you and asks input again.
    In register page you are considered as an employee and program asks you your title, name, school, and password. Name and password are important here because we going to use they when we try to login.
    Title must be at least 3 letter and max 5 letter also can not include numbers, symbols and space.
    Name must include only letters, there is no character limit and can include spaces but not consecutively spaces.
    Password must be contains at least 1 letter 1 number and 5 characters.
    Then we came to login page. we have to enter correct name and password if not we can't login and program warns us.
    If we successfully logged in now we can create a student, can see all students and employees and their's infos.
    If we try to a create student we need to pay attention to give a valid name.
    Students' ID are automaticly given to them starting from 1 and increases for every student.
    Students' average scores are automaticly calculating by program and gives them a letter grade starts from "AA" to "FF".
    Through show_all() method we can see all students and employees and thanks to tabulate library we can make a good design to our list.
    At the and we can press 0 and go back. In this program 0 is always used as escape button.
    If we want we can create(register) another employee and we can increase number of employees.
    After we came back to greeting page we can enter 0 and exit the program safely.

    Program Structure:
    I used an abstract class School. Student and Employee classes are inherits from it. There is a common function named "show_all". This function is a static function because it needs to hold all students and list them.
    name and school name is also common variables.
    In Student class I used a static list named "students" to keep all students and Employee class has "employees" similar to it.
    I divided the program into functions for easy to manage and I am confused about how to use main function I think it can be used in a different style.

    Testing:
    I used a lot of tests because I used regex several times and they need so many tests to be sure they are working.
    Thanks to pytest it was easy to testing

    Libraries:
    abc
    tabulate (run this command to use: pip install tabulate)
    re
    sys

    I did this project mostly to improve myself about OOP copcept in python and I think it worked.
