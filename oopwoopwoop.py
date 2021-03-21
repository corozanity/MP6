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
        # Different menus in program
        self.Menus = {"MainMenu": MainMenu(),
                      "InputProject": InputProject(),
                      "ViewProjects": ViewProjects(),
                      "ScheduleProjects": ScheduleProjects(),
                      "GetProject": GetProject()}

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
                clear()
                return "InputProject"
            elif choice == '2':
                clear()
                return "ViewProjects"
            elif choice == '3':
                clear()
                return "ScheduleProjects"
            elif choice == "4":
                clear()
                return "GetProject"
            elif choice == "5":
                exit()
            else:
                print("Invalid input. Please choose from the menu.")


class InputProject(Scene):
    def enter(self):
        print("Select one of the options: "
              "\n[1]Main menu"
              "\n[2]Input Project"
              "\n[3]Exit")
        while True:
            choice = input()
            if choice == "1":
                return "MainMenu"
            elif choice == "2":
                self.input_project()
                return "InputProject"
            elif choice == "3":
                exit()
            else:
                print("Select one of the options ")
                return "InputProject"

    def input_project(self):
        try:
            id_number = input("Enter ID Number:")
            csvreader = csv.reader(open("proj.csv", "r"))

            # Checks if user input is in ID column of csv file
            for row in csvreader:
                if id_number == row[0]:
                    print("\n", "ID already exists.", "\n")
                    return False

            project_title = input("Enter project title: ")
            project_size = input("Enter number of pages: ")
            project_priority = input("Enter priority: ")
            print()

            # Checks if all variable have values
            if id_number and project_title and project_size and project_priority:
                # Appends values to proj.csv
                file = open("proj.csv", "a", newline="\n")
                cwriter = csv.writer(file)
                cwriter.writerow([id_number, project_title, project_size, project_priority])
                file.close()
                print("Project successfully entered!", "\n")
            else:
                raise ValueError("Invalid Input\n")
        except ValueError as e:
            print(e)


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
                self.view_one_proj()
                return "ViewProjects"
            elif choice == "3":
                self.completed_proj()
                return "ViewProjects"
            elif choice == "4":
                self.all_proj()
                return "ViewProjects"
            elif choice == "5":
                exit()
            else:
                print("Select one of the options ")
                return "ViewProjects"

    def view_one_proj(self):
        try:
            input_id = int(input("Enter ID to be searched: "))
            data = pd.read_csv("proj.csv")

            # Checks if proj.csv file is empty
            if data[data['ID'] == input_id].empty:
                print("\nSorry, ID does not exist.\n")
            else:
                # Checks if user input matches a value in column ID
                res = data[data['ID'] == input_id]
                # Returns row of matched ID
                print("\n", res.to_string(index=False), "\n")
                return False
        except ValueError:
            print("Wrong Input")
            print()

    def all_proj(self):
        data = pd.read_csv("proj.csv")
        # Checks if proj.csv file is empty
        if data.empty:
            print('\nNo projects have been created.\n')
        else:
            # Returns all rows from proj.csv
            print("\n", data.to_string(index=False), "\n")

    def completed_proj(self):
        data = pd.read_csv("completed.csv")
        # Checks if completed.csv file is empty
        if data.empty:
            print('\nNo projects have been completed.\n')
        else:
            # Returns all rows from completed.csv
            print("\n", data.to_string(index=False), "\n")


class ScheduleProjects(Scene):
    def enter(self):
        print("Schedule Projects"
              "\n[1]MainMenu"
              "\n[2]Create Schedule"
              "\n[3]View Updated Schedule"
              "\n[4]Exit")
        while True:
            choice = input()
            if choice == "1":
                return "MainMenu"
            elif choice == "2":
                self.create_sched()
                return "ScheduleProjects"
            elif choice == "3":
                self.update_sched()
                return "ScheduleProjects"
            elif choice == "4":
                exit(0)
            else:
                print("Select one of the options ")
                return "ScheduleProjects"

    def create_sched(self):
        data = pd.read_csv("proj.csv")
        # Checks if proj.csv file is empty
        if data.empty:
            print('\nCannot create schedule. User must create a project first.\n')
        else:
            data2 = pd.read_csv("completed.csv")

            # get data that is in proj.csv
            # that doesn't exist in completed.csv
            concat_proj_sorted = pd.concat([data, data2])
            diff = concat_proj_sorted.drop_duplicates(subset=["ID"], keep=False)

            # Sorts values in sorted.csv by priority and size
            sorted_data = diff.sort_values(by=["Priority", "Size"], ascending=True)

            # Writes the sorted values on sorted.csv
            sorted_data.to_csv(r'sorted.csv', index=False)

            print("Schedule created!")
            print(pd.read_csv("sorted.csv").to_string(index=False))

    def update_sched(self):
        data = pd.read_csv("sorted.csv")
        # Sorts values in sorted.csv by priority and size
        sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
        # Writes the sorted values on sorted.csv
        sorted_data.to_csv('sorted.csv', mode='w', index=False)
        # Checks if sorted.csv file is empty
        if sorted_data.empty:
            print("\nA schedule has not been created. Create a schedule first.\n")
        else:
            # Returns all rows from sorted.csv
            print("\n", sorted_data.to_string(index=False), "\n")


class GetProject(Scene):
    def enter(self):
        data = pd.read_csv("sorted.csv")
        # Sorts values in sorted.csv by priority and size
        sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
        # Writes the sorted values on sorted.csv
        sorted_data.to_csv('sorted.csv', mode='w', index=False)
        # Checks if sorted.csv file is empty
        if sorted_data.empty:
            print("\nNo projects available in queue.\n")
            return "MainMenu"
        else:
            # getting first row
            test = sorted_data.head(1)
            # removing first row
            remove_row = sorted_data.iloc[1:]
            # saving new sorted.csv
            remove_row.to_csv("sorted.csv", index=False)
            print()
            print("Removing From Queue.....")
            print("Project:")
            # Returns the removed row from sorted.csv
            print(test.to_string(index=False))
            print()
            # Appends the removed row to completed.csv
            test.to_csv("completed.csv", mode="a", index=False, header=False)
            print("Updated Queue:")
            print("\n", sorted_data.to_string(index=False), "\n")
            return "MainMenu"


Letters().run()
