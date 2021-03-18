import csv
import pandas as pd


def menu():
    print("(1)Input Project Details")
    print("(2)View Projects")
    print("(3)Schedule Projects")
    print("(4)Get Project")
    print("(5)Exit")


def input_project():
    id_number = input("Enter ID Number: ")
    flag = True
    while flag:
        with open("proj.csv", "r") as infile:
            creader = csv.DictReader(infile, delimiter=",")
            for row in creader:
                while id_number in row['ID']:
                    print("ID already exists.")
                    id_number = input("Enter ID Number: ")

                else:
                    flag = False

    project_title = input("Enter project title: ")
    project_size = input("Enter number of pages: ")
    project_priority = input("Enter priority: ")
    print()
    infile.close()

    file = open("proj.csv", "a", newline="\n")
    cwriter = csv.writer(file)
    cwriter.writerow([id_number, project_title, project_size, project_priority])

    file.close()

    sortedfile = open("sorted.csv", "a", newline="\n")
    cwriter = csv.writer(sortedfile)
    cwriter.writerow([id_number, project_title, project_size, project_priority])


def view_proj_submenu():
    print("(1)One Project")
    print("(2)Show completed project")
    print("(3)Show all projects")


def view_one_proj():
    input_id = int(input("Enter ID to be searched: "))

    data = pd.read_csv("proj.csv")
    if data[data['ID'] == input_id].empty:
        print()
        print("Sorry, ID does not exist.")
        print()
    else:
        res = data[data['ID'] == input_id]
        print()
        print(res.to_string(index=False))
        print()


def completed_proj():
    data = pd.read_csv("completed.csv")
    if data.empty:
        print('DataFrame is empty')
    else:
        print()
        print(data.to_string(index=False))
        print()



def all_proj():
    data = pd.read_csv("proj.csv")
    print()
    print(data.to_string(index=False))
    print()


def sched_submenu():
    print("(1)Create Schedule")
    print("(2)View Updated Schedule")


def create_sched():
    data = pd.read_csv("proj.csv")
    data2 = pd.read_csv("completed.csv")

    # data - data2
    # proj.csv - completed.csv
    # anong meron sa proj na wla sa completed
    concat_proj_sorted = pd.concat([data, data2])
    diff = concat_proj_sorted.drop_duplicates(subset=["ID"], keep=False)

    sorted_data = diff.sort_values(by=["Priority", "Size"], ascending=True)
    sorted_data.to_csv(r'sorted.csv', index=False)

    print()


def update_sched():
    # create an exception here
    # if there is no schedule file
    # or nothing in first row of file
    # submenu31()
    data = pd.read_csv("sorted.csv")
    print(data.to_string(index=False))
    print()


def get_proj():
    # reading csv
    data = pd.read_csv("sorted.csv")
    sorted_data = data.sort_values(by=["Priority", "Size"], ascending=True)
    sorted_data.to_csv('sorted.csv', mode='w', index=False)
    # getting first row
    test = sorted_data.head(1)
    # removing first row
    remove_row = sorted_data.iloc[1:]

    # saving new csv
    remove_row.to_csv("sorted.csv", index=False)

    print("Getting Project.....")
    print("Project:")
    print(test.to_string(index=False))
    print()

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

        elif choice == "3":
            sched_submenu()

            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                create_sched()

            elif sub_choice == "2":
                update_sched()

        elif choice == "4":
            get_proj()

        elif choice == "5":
            exit()
            print()

        elif choice == "6":
            data = pd.read_csv("sorted.csv")
            print(data.values[1][1])

        else:
            print("Invalid Input")


main()
