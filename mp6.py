import csv
import pandas as pd
from numpy.ma import indices


def show_menu():
    print("(1)Input Project Details")
    print("(2)View Projects")
    print("(3)Schedule Projects")
    print("(4)Get Project")
    print("(5)Exit")


def enter_project():

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
    infile.close()

    file = open("proj.csv", "a", newline="\n")
    cwriter = csv.writer(file)
    cwriter.writerow([project_priority, project_title, project_size, id_number])

    file.close()


def show_submenu2():

    print("(1)One Project")
    print("(2)Show completed project")
    print("(3)Show all projects")


def submenu21(proj_id):

    file = open("proj.csv", "r", encoding='utf-8-sig')
    table = csv.DictReader(file)
    proj = {}

    try:
        for row in table:
            proj[row["ID"]] = {k: v for k, v in row.items() if k != 'ID'}
        print(proj[proj_id])
        print()
    except KeyError:
        print("ID does not exist.")
        print()

    file.close()


def submenu22():

    data = pd.read_csv("completed.csv")
    print(data.to_string(index=False))
    print()

def submenu23():

    data = pd.read_csv("proj.csv")
    print(data.to_string(index=False))
    print()


def show_submenu3():

    print("(1)Create Schedule")
    print("(2)View Updated Schedule")


def submenu31():

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

    # reference:
    # https://pandas.pydata.org/docs/reference/api/pandas.concat.html


def submenu32():

    # create an exception here
    # if there is no schedule file
    # or nothing in first row of file
    # submenu31()
    data = pd.read_csv("sorted.csv")
    print(data.to_string(index=False))
    print()


def submenu4():

    # reading csv
    data = pd.read_csv("sorted.csv")
    # getting first row
    test = data.head(1)
    # removing first row
    data = data.iloc[1:]
    next = data.head(1)

    # saving new csv
    data.to_csv("sorted.csv", index=False)

    print(next)

    test.to_csv("completed.csv", mode="a", index=False, header=False)


def main():

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            enter_project()

        elif choice == "2":
            show_submenu2()
            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                input_id = int(input("Enter ID to be searched: "))
                submenu21(str(input_id))

            elif sub_choice == "2":
                submenu22()

            elif sub_choice == "3":
                submenu23()

        elif choice == "3":
            show_submenu3()

            sub_choice = input("Enter your choice: ")
            if sub_choice == "1":
                submenu31()

            elif sub_choice == "2":
                submenu32()

        elif choice == "4":
            submenu4()
            print()

        elif choice == "5":
            exit()
            print()

        elif choice == "6":
            print()

        else:
            print("Invalid Input")


main()
