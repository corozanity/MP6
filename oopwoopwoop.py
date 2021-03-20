import csv
import pandas as pd
from os import system, name


# define our clear function
# https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Letters(object):
    def __init__(self):
        self.Menus = {"MainMenu": MainMenu(), "InputProject": InputProject(),
                      "ViewProjects": ViewProjects(), "ScheduleProjects": ScheduleProjects()}  # Different menus in program

    def run(self):
        start = "MainMenu"
        while True:
            start = self.Menus.get(start).enter()


class Scene(object):
    def enter(self):
        exit(0)


class MainMenu(Scene):
    def enter(self):
        print("Main Menu"
              "\n[1]Input Project Details"
              "\n[2]View Projects"
              "\n[3]Schedule Projects"
              "\n[4]Get Project"
              "\n[5]Exit")
        while True:
            choice = input("Input:")
            if choice == '1':
                return "InputProject"
                # Input_Project().enter()
            elif choice == '2':
                clear()
                return "ViewProjects"
            elif choice == '3':
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                exit()
            else:
                print("Select one of the choices ")


class InputProject(Scene):
    def enter(self):
        print("Select one of the options: "
              "\n[1]Mainmenu"
              "\nMenuB"
              "\nMenuC"
              "\nexit")
        while True:
            choice = input()
            choice = choice.lower()
            if choice == "1":
                return "MainMenu"
            elif choice == "2":
                ViewProjects.enter()
            elif choice == "3":
                return "MenuC"
            elif choice == "4":
                pass
            elif choice == "exit":
                exit(0)
            else:
                print("Select one of the options ")
                return "Input_Project"


class ViewProjects(Scene):
    def enter(self):
        print("View Projects"
              "\n[1]Main Menu"
              "\n[2]One Project"
              "\n[3]Completed Projects"
              "\n[4]All Projects"
              "\n[5]Exit")
        while True:
            choice = input()
            if choice == "1":
                return "MainMenu"
            elif choice == "2":
                return "InputProject"
            elif choice == "3":
                return "MenuC"
            elif choice == "4":
                exit(0)
            else:
                print("Select one of the options ")


class ScheduleProjects(Scene):
    def enter(self):
        print("Schedule Projects"
              "\n[1]MainMenu"
              "\n[2]Create Schedule"
              "\n[3]View Updated Schedule"
              "\n[4]exit")
        while True:
            choice = input()
            choice = choice.lower()
            if choice == "1":
                return "MainMenu"
            elif choice == "2":
                pass
                # return "CreateSchedule"
            elif choice == "3":
                pass
                # return "ViewUpdatedSchedule"
            elif choice == "exit":
                exit(0)
            else:
                print("Select one of the options ")


Letters().run()
