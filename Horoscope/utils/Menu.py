from businness.Horoscope import Horoscope
from student.Student import Student
from utils.FactoryType import FactoryType
from dao.DaoFactory import DaoFactory


class Menu:
    def run_menu(self):
        self.menu()

    def menu_message(self):
        print("\nPlease select an option from the menu")
        print("1.Print the horoscope for all players")
        print("2.Get a student after name")
        print("3. Add a student")
        print("4. Print all the students")
        print("5. Exit")

    def menu(self):
        while True:
            h = Horoscope()
            factory_type = int(input("Please enter a factory_type(1 - XML, 2 - SQL): \n"))
            self.menu_message()
            option = int(input("Selected value: "))
            student_repo = DaoFactory.get_dao_factory(FactoryType(factory_type)).get_student_base_repo()
            if option == 1:
                h.execute(FactoryType(factory_type))
            elif option == 2:
                searched_name = str(input("Enter the name of the student: "))
                student = student_repo.get_student_after_name(searched_name)
                if student is not None:
                    print("Searched name is: [" + str(student.name) + "]")
                else:
                    print("The searched name: [" + str(searched_name) + "] was not found!\n")
            elif option == 3:
                searched_name = str(input("Enter the name of the student: "))
                student_repo.add_student(Student(searched_name))
            elif option == 4:
                print("The list will all the students: ")
                for stud in student_repo.get_all_students():
                    print(stud.name)
                print("\n")
            elif option == 5:
                print("You chose to exit the program, bye!")
                break
