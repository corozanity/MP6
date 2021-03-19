import csv
import pandas as pd


def menu():
    print("(1)Input Project Details")
    print("(2)View Projects")
    print("(3)Schedule Projects")
    print("(4)Get Project")
    print("(5)Exit")


def input_project():
    id_number = input("Enter ID Number:")
    csvreader = csv.reader(open("proj.csv", "r"))

    try:
        # Checks if user input is in ID column of csv file
        for row in csvreader:
            if id_number == row[0]:
                print("ID already exists.")
                print()
                main()

        project_title = input("Enter project title: ")
        project_size = input("Enter number of pages: ")
        project_priority = input("Enter priority: ")
        print()

        # Appends values to proj.csv
        file = open("proj.csv", "a", newline="\n")
        cwriter = csv.writer(file)
        cwriter.writerow([id_number, project_title, project_size, project_priority])
        file.close()

        # Appends values to sorted.csv
        sortedfile = open("sorted.csv", "a", newline="\n")
        csvwriter = csv.writer(sortedfile)
        csvwriter.writerow([id_number, project_title, project_size, project_priority])
        sortedfile.close()

    # Handles error if csv file is empty
    except IndexError:
        project_title = input("Enter project title: ")
        project_size = input("Enter number of pages: ")
        project_priority = input("Enter priority: ")
        print()

        # Appends values to proj.csv
        file = open("proj.csv", "a", newline="\n")
        cwriter = csv.writer(file)
        cwriter.writerow([id_number, project_title, project_size, project_priority])
        file.close()

        # Appends values to sorted.csv
        sortedfile = open("sorted.csv", "a", newline="\n")
        csvwriter = csv.writer(sortedfile)
        csvwriter.writerow([id_number, project_title, project_size, project_priority])
        sortedfile.close()


def view_proj_submenu():
    print("(1)One Project")
    print("(2)Show completed project")
    print("(3)Show all projects")


def view_one_proj():
    input_id = int(input("Enter ID to be searched: "))
    data = pd.read_csv("proj.csv")

    # Checks if proj.csv file is empty
    if data[data['ID'] == input_id].empty:
        print()
        print("Sorry, ID does not exist.")
        print()
    else:
        # Checks if user input matches a value in column ID
        res = data[data['ID'] == input_id]
        print()
        # Returns row of matched ID
        print(res.to_string(index=False))
        print()


def completed_proj():
    data = pd.read_csv("completed.csv")
    # Checks if completed.csv file is empty
    if data.empty:
        print()
        print('No projects have been completed.')
        print()
    else:
        print()
        # Returns all rows from completed.csv
        print(data.to_string(index=False))
        print()


def all_proj():
    data = pd.read_csv("proj.csv")
    # Checks if proj.csv file is empty
    if data.empty:
        print()
        print('No projects have been created.')
        print()
    else:
        print()
        # Returns all rows from proj.csv
        print(data.to_string(index=False))
        print()


def sched_submenu():
    print("(1)Create Schedule")
    print("(2)View Updated Schedule")


def create_sched():
    data = pd.read_csv("sorted.csv")
    # Checks if sorted.csv file is empty
    if data.empty:
        print()
        print('Cannot create schedule. User must create a project first.')
        print()
    else:
        # Sorts values in sorted.csv by priority and size
        sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
        # Writes the sorted values on sorted.csv
        sorted_data.to_csv(r'sorted.csv', index=False)
        print()
        print("Schedule created, you can view updated schedule now.")
        print()


def update_sched():
    data = pd.read_csv("sorted.csv")
    # Sorts values in sorted.csv by priority and size
    sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
    # Writes the sorted values on sorted.csv
    sorted_data.to_csv('sorted.csv', mode='w', index=False)
    # Checks if sorted.csv file is empty
    if sorted_data.empty:
        print()
        print("A schedule has not been created. Create a schedule first.")
        print()
    else:
        print()
        # Returns all rows from sorted.csv
        print(sorted_data.to_string(index=False))
        print()


def get_proj():
    data = pd.read_csv("sorted.csv")
    # Sorts values in sorted.csv by priority and size
    sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
    # Writes the sorted values on sorted.csv
    sorted_data.to_csv('sorted.csv', mode='w', index=False)
    # Checks if sorted.csv file is empty
    if sorted_data.empty:
        print("No projects available in queue.")
        print()
    else:
        # getting first row
        test = sorted_data.head(1)
        # removing first row
        remove_row = sorted_data.iloc[1:]
        # saving new sorted.csv
        remove_row.to_csv("sorted.csv", index=False)
        print("Getting Project.....")
        print("Project:")
        # Returns the removed row from sorted.csv
        print(test.to_string(index=False))
        print()
        # Appends the removed row to completed.csv
        test.to_csv("completed.csv", mode="a", index=False, header=False)


def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            input_project()

        elif choice == "2":
            view_proj_submenu()
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                view_one_proj()

            elif sub_choice == "2":
                completed_proj()

            elif sub_choice == "3":
                all_proj()

            else:
                print("Invalid Input")
                print()

        elif choice == "3":
            sched_submenu()

            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                create_sched()

            elif sub_choice == "2":
                update_sched()

            else:
                print("Invalid Input")
                print()

        elif choice == "4":
            get_proj()

        elif choice == "5":
            exit()
            print()

        else:
            print("Invalid Input")


main()
